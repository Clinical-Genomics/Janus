import mock
import sys
import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Janus"
copyright = "2024, Christian Oertlin"
author = "Christian Oertlin"
release = "0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Enables autodoc to process docstrings from modules
    "sphinx.ext.napoleon",  # Allows Google-style or NumPy-style docstrings
    "sphinx.ext.viewcode",  # Links to source code in the documentation (optional)
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

sys.path.insert(0, os.path.abspath(".."))


MOCK_MODULES = []
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
