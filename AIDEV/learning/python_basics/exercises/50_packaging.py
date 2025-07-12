"""
Bài tập 50: Packaging

Mục tiêu:
- Hiểu cách tạo package trong Python
- Thực hành với setup.py và requirements.txt
- Sử dụng packaging tools
"""

import os
import sys
import time
import pytest
import unittest
import logging
import traceback
import pdb
import psutil
import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re
from functools import wraps
from contextlib import contextmanager

# TODO: Package structure
def package_structure():
    """
    Package structure example.
    
    mypackage/
    ├── setup.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    ├── MANIFEST.in
    ├── mypackage/
    │   ├── __init__.py
    │   ├── core.py
    │   └── utils.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_core.py
    └── docs/
        ├── conf.py
        └── index.rst
    """
    return "Done"

# TODO: setup.py
def setup_py():
    """
    setup.py example.
    
    from setuptools import setup, find_packages
    
    setup(
        name="mypackage",
        version="0.1.0",
        packages=find_packages(),
        install_requires=[
            "numpy>=1.19.0",
            "pandas>=1.0.0",
            "requests>=2.25.0",
        ],
        extras_require={
            "dev": [
                "pytest>=6.0.0",
                "pytest-cov>=2.0.0",
                "black>=20.0.0",
                "isort>=5.0.0",
                "mypy>=0.800",
            ],
            "docs": [
                "sphinx>=3.0.0",
                "sphinx-rtd-theme>=0.5.0",
            ],
        },
        python_requires=">=3.7",
        author="Your Name",
        author_email="your.email@example.com",
        description="A short description of the package",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/yourusername/mypackage",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    )
    """
    return "Done"

# TODO: requirements.txt
def requirements_txt():
    """
    requirements.txt example.
    
    numpy>=1.19.0
    pandas>=1.0.0
    requests>=2.25.0
    pytest>=6.0.0
    pytest-cov>=2.0.0
    black>=20.0.0
    isort>=5.0.0
    mypy>=0.800
    sphinx>=3.0.0
    sphinx-rtd-theme>=0.5.0
    """
    return "Done"

# TODO: README.md
def readme_md():
    """
    README.md example.
    
    # MyPackage
    
    A short description of the package.
    
    ## Installation
    
    ```bash
    pip install mypackage
    ```
    
    ## Usage
    
    ```python
    from mypackage import core
    
    result = core.main_function()
    print(result)
    ```
    
    ## Development
    
    ```bash
    git clone https://github.com/yourusername/mypackage.git
    cd mypackage
    pip install -e ".[dev]"
    pytest
    ```
    
    ## Documentation
    
    ```bash
    pip install -e ".[docs]"
    cd docs
    make html
    ```
    
    ## License
    
    This project is licensed under the MIT License - see the LICENSE file for details.
    """
    return "Done"

# TODO: LICENSE
def license_file():
    """
    LICENSE example.
    
    MIT License
    
    Copyright (c) 2021 Your Name
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """
    return "Done"

# TODO: MANIFEST.in
def manifest_in():
    """
    MANIFEST.in example.
    
    include LICENSE
    include README.md
    include requirements.txt
    include docs/conf.py
    include docs/index.rst
    recursive-include docs *
    recursive-include tests *
    """
    return "Done"

# TODO: __init__.py
def init_py():
    """
    __init__.py example.
    
    """
    """
    MyPackage
    
    A short description of the package.
    """
    
    __version__ = "0.1.0"
    __author__ = "Your Name"
    __email__ = "your.email@example.com"
    
    from .core import main_function
    from .utils import helper_function
    
    __all__ = ["main_function", "helper_function"]
    """
    return "Done"

# TODO: core.py
def core_py():
    """
    core.py example.
    
    def main_function():
        \"\"\"
        Main function of the package.
        
        Returns:
            str: A string value
        \"\"\"
        return "Hello, World!"
    """
    return "Done"

# TODO: utils.py
def utils_py():
    """
    utils.py example.
    
    def helper_function():
        \"\"\"
        Helper function of the package.
        
        Returns:
            str: A string value
        \"\"\"
        return "Helper"
    """
    return "Done"

# TODO: test_core.py
def test_core_py():
    """
    test_core.py example.
    
    import pytest
    from mypackage.core import main_function
    
    def test_main_function():
        assert main_function() == "Hello, World!"
    """
    return "Done"

# TODO: conf.py
def conf_py():
    """
    conf.py example.
    
    import os
    import sys
    sys.path.insert(0, os.path.abspath(".."))
    
    project = "MyPackage"
    copyright = "2021, Your Name"
    author = "Your Name"
    
    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.viewcode",
    ]
    
    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
    
    html_theme = "sphinx_rtd_theme"
    html_static_path = ["_static"]
    """
    return "Done"

# TODO: index.rst
def index_rst():
    """
    index.rst example.
    
    Welcome to MyPackage's documentation!
    ====================================
    
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
    
       installation
       usage
       api
    
    Indices and tables
    =================
    
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    """
    return "Done"

# TODO: Example usage
def example_usage():
    """
    Example usage of packaging features.
    """
    # Package structure
    print("Package structure:")
    print(package_structure())
    
    # setup.py
    print("\nsetup.py:")
    print(setup_py())
    
    # requirements.txt
    print("\nrequirements.txt:")
    print(requirements_txt())
    
    # README.md
    print("\nREADME.md:")
    print(readme_md())
    
    # LICENSE
    print("\nLICENSE:")
    print(license_file())
    
    # MANIFEST.in
    print("\nMANIFEST.in:")
    print(manifest_in())
    
    # __init__.py
    print("\n__init__.py:")
    print(init_py())
    
    # core.py
    print("\ncore.py:")
    print(core_py())
    
    # utils.py
    print("\nutils.py:")
    print(utils_py())
    
    # test_core.py
    print("\ntest_core.py:")
    print(test_core_py())
    
    # conf.py
    print("\nconf.py:")
    print(conf_py())
    
    # index.rst
    print("\nindex.rst:")
    print(index_rst())

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo package cho một ứng dụng FastAPI
2. Tạo package cho một ứng dụng machine learning
3. Tạo package cho một hệ thống microservices
4. Tạo package cho một ứng dụng web với Nginx
5. Tạo package cho một hệ thống database
""" 