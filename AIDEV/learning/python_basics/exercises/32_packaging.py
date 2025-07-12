"""
Bài tập 32: Packaging

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

# TODO: Package structure
"""
Package structure example:

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

# TODO: setup.py
"""
setup.py example:

from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.19.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
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

# TODO: requirements.txt
"""
requirements.txt example:

requests>=2.25.1
pandas>=1.2.0
numpy>=1.19.0
pytest>=6.0.0
black>=21.0.0
flake8>=3.9.0
"""

# TODO: README.md
"""
README.md example:

# My Package

A short description of your package.

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package import core

result = core.my_function()
print(result)
```

## Development

```bash
git clone https://github.com/yourusername/my_package.git
cd my_package
pip install -e .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
"""

# TODO: LICENSE
"""
LICENSE example (MIT License):

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

# TODO: MANIFEST.in
"""
MANIFEST.in example:

include LICENSE
include README.md
include requirements.txt
recursive-include docs *
recursive-include tests *
"""

# TODO: __init__.py
"""
__init__.py example:

from .core import my_function
from .utils import helper_function

__version__ = "0.1.0"
__author__ = "Your Name"
"""

# TODO: core.py
"""
core.py example:

def my_function():
    \"\"\"
    Main function of the package.
    
    Returns:
        str: A greeting message
    \"\"\"
    return "Hello from my_package!"
"""

# TODO: utils.py
"""
utils.py example:

def helper_function():
    \"\"\"
    Helper function for the package.
    
    Returns:
        str: A helper message
    \"\"\"
    return "I'm here to help!"
"""

# TODO: test_core.py
"""
test_core.py example:

import pytest
from my_package import core

def test_my_function():
    assert core.my_function() == "Hello from my_package!"
"""

# TODO: conf.py
"""
conf.py example:

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'My Package'
copyright = '2021, Your Name'
author = 'Your Name'
version = '0.1.0'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
"""

# TODO: index.rst
"""
index.rst example:

Welcome to My Package's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

# TODO: Example usage
def example_usage():
    """
    Example usage of packaging features.
    """
    # Package structure
    print("Package structure:")
    print("""
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
    """)
    
    # setup.py
    print("\nsetup.py:")
    print("""
    from setuptools import setup, find_packages

    setup(
        name="my_package",
        version="0.1.0",
        packages=find_packages(),
        install_requires=[
            "requests>=2.25.1",
            "pandas>=1.2.0",
            "numpy>=1.19.0",
        ],
        author="Your Name",
        author_email="your.email@example.com",
        description="A short description of your package",
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
    """)
    
    # requirements.txt
    print("\nrequirements.txt:")
    print("""
    requests>=2.25.1
    pandas>=1.2.0
    numpy>=1.19.0
    pytest>=6.0.0
    black>=21.0.0
    flake8>=3.9.0
    """)
    
    # README.md
    print("\nREADME.md:")
    print("""
    # My Package

    A short description of your package.

    ## Installation

    ```bash
    pip install my_package
    ```

    ## Usage

    ```python
    from my_package import core

    result = core.my_function()
    print(result)
    ```

    ## Development

    ```bash
    git clone https://github.com/yourusername/my_package.git
    cd my_package
    pip install -e .
    ```

    ## License

    This project is licensed under the MIT License - see the LICENSE file for details.
    """)
    
    # LICENSE
    print("\nLICENSE:")
    print("""
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
    """)
    
    # MANIFEST.in
    print("\nMANIFEST.in:")
    print("""
    include LICENSE
    include README.md
    include requirements.txt
    recursive-include docs *
    recursive-include tests *
    """)
    
    # __init__.py
    print("\n__init__.py:")
    print("""
    from .core import my_function
    from .utils import helper_function

    __version__ = "0.1.0"
    __author__ = "Your Name"
    """)
    
    # core.py
    print("\ncore.py:")
    print("""
    def my_function():
        \"\"\"
        Main function of the package.
        
        Returns:
            str: A greeting message
        \"\"\"
        return "Hello from my_package!"
    """)
    
    # utils.py
    print("\nutils.py:")
    print("""
    def helper_function():
        \"\"\"
        Helper function for the package.
        
        Returns:
            str: A helper message
        \"\"\"
        return "I'm here to help!"
    """)
    
    # test_core.py
    print("\ntest_core.py:")
    print("""
    import pytest
    from my_package import core

    def test_my_function():
        assert core.my_function() == "Hello from my_package!"
    """)
    
    # conf.py
    print("\nconf.py:")
    print("""
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

    project = 'My Package'
    copyright = '2021, Your Name'
    author = 'Your Name'
    version = '0.1.0'
    release = '0.1.0'

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
    ]

    templates_path = ['_templates']
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
    html_theme = 'sphinx_rtd_theme'
    html_static_path = ['_static']
    """)
    
    # index.rst
    print("\nindex.rst:")
    print("""
    Welcome to My Package's documentation!
    =====================================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       installation
       usage
       api

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
    """)

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