project = "GNews"
copyright = "2026, Muhammad Abdullah"
author = "Muhammad Abdullah"
release = "0.8.2"

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
