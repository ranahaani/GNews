from pathlib import Path

project = "GNews"
copyright = "2026, Muhammad Abdullah"
author = "Muhammad Abdullah"

# Keep the docs version aligned with the package so a release bump cannot
# leave /en/latest/ advertising an older release.
_setup_py = Path(__file__).resolve().parent.parent.joinpath("setup.py").read_text(encoding="utf-8")
release = None
for _line in _setup_py.splitlines():
    _stripped = _line.strip()
    if _stripped.startswith("version=") or _stripped.startswith("version ="):
        release = _stripped.split("=", 1)[1].strip().strip(",").strip("'\"")
        break
if not release:
    raise RuntimeError("Could not read version from setup.py")

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "logo_only": False,
    "navigation_depth": 4,
}
