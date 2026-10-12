# -*- coding: utf-8 -*-
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

import os

# Load metadata from __init__.py
base_dir = os.path.dirname(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "verspec", "__init__.py")) as f:
    exec(f.read(), about)

# General information about the project.
project = "verspec"
version = release = about["__version__"]
copyright = about["__copyright__"]

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
]
