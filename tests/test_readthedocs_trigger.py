"""Decision table for the Read the Docs trigger script."""

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / ".github" / "scripts" / "trigger_readthedocs.py"


def _load():
    spec = importlib.util.spec_from_file_location("trigger_readthedocs", _SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_version_slug_matches_readthedocs_rules():
    module = _load()
    assert module.version_slug("0.8.3") == "0.8.3"
    assert module.version_slug("v0.8.3") == "v0.8.3"
    assert module.version_slug("docs/readthedocs") == "docs-readthedocs"
    assert module.version_slug("Asto7-master") == "asto7-master"
    assert module.version_slug("release/1.0") == "release-1.0"


def test_master_push_targets_latest():
    module = _load()
    assert module.resolve_slug("push", "branch", "master", "") == "latest"


def test_tag_and_release_target_the_tag_slug():
    module = _load()
    assert module.resolve_slug("push", "tag", "0.8.3", "") == "0.8.3"
    assert module.resolve_slug("release", "tag", "ignored", "v1.2.3") == "v1.2.3"


def test_workflow_dispatch_uses_the_requested_version_not_the_branch():
    module = _load()
    assert module.resolve_slug("workflow_dispatch", "branch", "master", "", "latest") == "latest"
    assert module.resolve_slug("workflow_dispatch", "branch", "master", "", "0.8.3") == "0.8.3"


def test_missing_token_skips(monkeypatch, capsys):
    monkeypatch.delenv("READTHEDOCS_TOKEN", raising=False)
    module = _load()
    assert module.main() == 0
    assert "skipping" in capsys.readouterr().out.lower()


def test_latest_only_posts_a_build(monkeypatch):
    monkeypatch.setenv("READTHEDOCS_TOKEN", "token")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "push")
    monkeypatch.setenv("GITHUB_REF_TYPE", "branch")
    monkeypatch.setenv("GITHUB_REF_NAME", "master")
    module = _load()
    calls = []

    def fake_request(token, method, path, body=None):
        calls.append((method, path, body))
        return 202, {"build": {"id": 42}}

    monkeypatch.setattr(module, "_request", fake_request)
    assert module.main() == 0
    assert calls == [("POST", "/versions/latest/builds/", None)]


def test_inactive_tag_is_activated_instead_of_posted(monkeypatch):
    monkeypatch.setenv("READTHEDOCS_TOKEN", "token")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "release")
    monkeypatch.setenv("RELEASE_TAG", "0.8.3")
    module = _load()
    calls = []
    responses = [
        (202, {}),
        (200, {"active": False}),
        (200, {"active": True}),
    ]

    def fake_request(token, method, path, body=None):
        calls.append((method, path, body))
        return responses.pop(0)

    monkeypatch.setattr(module, "_request", fake_request)
    assert module.main() == 0
    assert calls == [
        ("POST", "/sync-versions/", None),
        ("GET", "/versions/0.8.3/", None),
        ("PATCH", "/versions/0.8.3/", {"active": True}),
    ]


def test_active_tag_posts_a_build(monkeypatch):
    monkeypatch.setenv("READTHEDOCS_TOKEN", "token")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "push")
    monkeypatch.setenv("GITHUB_REF_TYPE", "tag")
    monkeypatch.setenv("GITHUB_REF_NAME", "v0.8.3")
    module = _load()
    calls = []
    responses = [
        (202, {}),
        (200, {"active": True}),
        (202, {"build": {"id": 7}}),
    ]

    def fake_request(token, method, path, body=None):
        calls.append((method, path, body))
        return responses.pop(0)

    monkeypatch.setattr(module, "_request", fake_request)
    assert module.main() == 0
    assert calls[-1] == ("POST", "/versions/v0.8.3/builds/", None)


def test_unsupported_event_exits(monkeypatch):
    monkeypatch.setenv("READTHEDOCS_TOKEN", "token")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "issues")
    module = _load()
    with pytest.raises(SystemExit):
        module.main()
