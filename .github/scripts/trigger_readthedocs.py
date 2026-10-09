#!/usr/bin/env python3
"""Trigger a Read the Docs build for the gnews project.

Master pushes build the ``latest`` version. Published releases and git tags
build the matching version slug. Exits 0 when ``READTHEDOCS_TOKEN`` is unset
so forks and unconfigured checkouts do not fail CI.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

PROJECT_SLUG = "gnews"
API_ROOT = f"https://readthedocs.org/api/v3/projects/{PROJECT_SLUG}"
# RTD syncs versions in the background. A public repo usually shows up well
# inside this window; past it, the GitHub integration needs a manual resync.
VERSION_SYNC_ATTEMPTS = 18
VERSION_SYNC_INTERVAL_SECONDS = 5


def version_slug(source: str) -> str:
    """Approximate Read the Docs' version slug for a tag or branch name.

    Slashes and a few other URL-breaking characters become dashes, the result
    is lowercased, and dots/underscores are preserved (``0.8.3`` stays
    ``0.8.3``, ``release/1.0`` becomes ``release-1.0``).
    """
    normalized = re.sub(r"[/%!?]", "-", source).lower()
    slug = re.sub(r"[^a-z0-9._-]+", "-", normalized)
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    return slug or "unknown"


def resolve_slug(
    event: str,
    ref_type: str,
    ref_name: str,
    release_tag: str,
    requested_version: str = "",
) -> str:
    """Return the RTD version slug this GitHub event should build."""
    # workflow_dispatch passes an explicit slug. GITHUB_REF_NAME is the branch
    # the workflow was run from (usually master), which is not a docs version.
    if event == "workflow_dispatch":
        name = requested_version.strip() or "latest"
        return "latest" if name == "latest" else version_slug(name)
    if event == "push" and ref_type != "tag":
        return "latest"
    if event == "release":
        name = release_tag or ref_name
    elif event == "push" and ref_type == "tag":
        name = ref_name
    else:
        raise SystemExit(f"Unsupported GitHub event {event!r}; not triggering a build.")

    if not name:
        raise SystemExit("No tag name on this event; not triggering a build.")
    return version_slug(name)


def _request(token: str, method: str, path: str, body: dict | None = None) -> tuple[int, object]:
    url = API_ROOT + path
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(url, data=data, method=method)
    request.add_header("Authorization", f"Token {token}")
    request.add_header("Accept", "application/json")
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode()
            payload: object = json.loads(raw) if raw else None
            return response.status, payload
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors="replace")
        try:
            payload = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            payload = raw
        return exc.code, payload


def _version_path(slug: str) -> str:
    return "/versions/" + urllib.parse.quote(slug, safe="._-") + "/"


def trigger_build(token: str, slug: str) -> tuple[int, object]:
    return _request(token, "POST", _version_path(slug) + "builds/")


def wait_for_version(token: str, slug: str) -> dict | None:
    path = _version_path(slug)
    for attempt in range(1, VERSION_SYNC_ATTEMPTS + 1):
        status, payload = _request(token, "GET", path)
        if status == 200 and isinstance(payload, dict):
            return payload
        if status != 404:
            print(f"Unexpected response looking up {slug} (HTTP {status}): {payload}")
            return None
        print(f"Version {slug} not visible yet (attempt {attempt}/{VERSION_SYNC_ATTEMPTS}).")
        if attempt != VERSION_SYNC_ATTEMPTS:
            time.sleep(VERSION_SYNC_INTERVAL_SECONDS)
    return None


def _report_trigger(slug: str, status: int, payload: object) -> int:
    if status == 202:
        build_id = None
        if isinstance(payload, dict):
            build = payload.get("build")
            if isinstance(build, dict):
                build_id = build.get("id")
        if build_id is not None:
            print(f"Triggered Read the Docs build {build_id} for version {slug}.")
        else:
            print(f"Triggered Read the Docs build for version {slug}.")
        return 0
    print(f"Failed to trigger version {slug} (HTTP {status}): {payload}")
    return 1


def main() -> int:
    token = os.environ.get("READTHEDOCS_TOKEN", "").strip()
    if not token:
        print("READTHEDOCS_TOKEN is not set; skipping Read the Docs build trigger.")
        return 0

    slug = resolve_slug(
        os.environ.get("GITHUB_EVENT_NAME", ""),
        os.environ.get("GITHUB_REF_TYPE", ""),
        os.environ.get("GITHUB_REF_NAME", ""),
        os.environ.get("RELEASE_TAG", ""),
        os.environ.get("RTD_VERSION", ""),
    )
    print(f"Read the Docs target version: {slug}")

    if slug != "latest":
        # A new tag is not a version until RTD syncs the repo. The webhook that
        # normally does this is what we are replacing, so sync explicitly.
        status, payload = _request(token, "POST", "/sync-versions/")
        if status != 202:
            print(f"Version sync failed (HTTP {status}): {payload}")
            return 1
        version = wait_for_version(token, slug)
        if version is None:
            print(
                f"Version {slug!r} did not appear after syncing. Reconnect the "
                "GitHub integration on the Read the Docs project and resync versions."
            )
            return 1
        if not version.get("active"):
            # Activating an inactive version queues its build. POSTing a build
            # against an inactive version returns 400.
            status, payload = _request(token, "PATCH", _version_path(slug), {"active": True})
            if status not in (200, 204):
                print(f"Activating version {slug} failed (HTTP {status}): {payload}")
                return 1
            print(f"Activated {slug}; Read the Docs builds a version when it is activated.")
            return 0

    status, payload = trigger_build(token, slug)
    return _report_trigger(slug, status, payload)


if __name__ == "__main__":
    sys.exit(main())
