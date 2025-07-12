"""
Bài tập 44: Packaging

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
    
    my_package/
    ├── setup.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    ├── MANIFEST.in
    ├── my_package/
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
    return "Package structure"

# TODO: setup.py
def setup_py():
    """
    setup.py example.
    
    from setuptools import setup, find_packages
    
    setup(
        name="my_package",
        version="0.1.0",
        packages=find_packages(),
        install_requires=[
            "requests>=2.25.1",
            "numpy>=1.19.5",
            "pandas>=1.2.0",
        ],
        extras_require={
            "dev": [
                "pytest>=6.0.0",
                "black>=20.8b1",
                "isort>=5.7.0",
            ],
        },
        author="Your Name",
        author_email="your.email@example.com",
        description="A short description of the package",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/yourusername/my_package",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
    )
    """
    return "setup.py"

# TODO: requirements.txt
def requirements_txt():
    """
    requirements.txt example.
    
    requests>=2.25.1
    numpy>=1.19.5
    pandas>=1.2.0
    pytest>=6.0.0
    black>=20.8b1
    isort>=5.7.0
    """
    return "requirements.txt"

# TODO: README.md
def readme_md():
    """
    README.md example.
    
    # My Package
    
    A short description of the package.
    
    ## Installation
    
    ```bash
    pip install my_package
    ```
    
    ## Usage
    
    ```python
    from my_package import core
    
    result = core.main()
    print(result)
    ```
    
    ## Development
    
    ```bash
    git clone https://github.com/yourusername/my_package.git
    cd my_package
    pip install -e ".[dev]"
    pytest
    ```
    
    ## License
    
    This project is licensed under the MIT License - see the LICENSE file for details.
    """
    return "README.md"

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
    return "LICENSE"

# TODO: MANIFEST.in
def manifest_in():
    """
    MANIFEST.in example.
    
    include LICENSE
    include README.md
    include requirements.txt
    recursive-include docs *
    recursive-include tests *
    """
    return "MANIFEST.in"

# TODO: __init__.py
def init_py():
    """
    __init__.py example.
    
    from .core import main
    from .utils import helper
    
    __version__ = "0.1.0"
    __author__ = "Your Name"
    """
    return "__init__.py"

# TODO: core.py
def core_py():
    """
    core.py example.
    
    def main():
        \"\"\"
        Main function.
        
        Returns:
            str: A message
        \"\"\"
        return "Hello, World!"
    """
    return "core.py"

# TODO: utils.py
def utils_py():
    """
    utils.py example.
    
    def helper():
        \"\"\"
        Helper function.
        
        Returns:
            str: A message
        \"\"\"
        return "Helper function"
    """
    return "utils.py"

# TODO: test_core.py
def test_core_py():
    """
    test_core.py example.
    
    import pytest
    from my_package.core import main
    
    def test_main():
        assert main() == "Hello, World!"
    """
    return "test_core.py"

# TODO: conf.py
def conf_py():
    """
    conf.py example.
    
    import os
    import sys
    sys.path.insert(0, os.path.abspath(".."))
    
    project = "My Package"
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
    return "conf.py"

# TODO: index.rst
def index_rst():
    """
    index.rst example.
    
    Welcome to My Package's documentation!
    =====================================
    
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
    return "index.rst"

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