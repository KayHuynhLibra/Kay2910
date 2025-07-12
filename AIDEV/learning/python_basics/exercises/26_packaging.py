"""
Bài tập 26: Packaging

Mục tiêu:
- Hiểu cách tạo package trong Python
- Thực hành với setup.py và requirements.txt
- Sử dụng packaging tools
"""

import os
import sys
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Package structure
"""
my_package/
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
├── MANIFEST.in
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── tests/
│       ├── __init__.py
│       └── test_core.py
└── docs/
    ├── conf.py
    └── index.rst
"""

# TODO: setup.py
"""
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
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.9.0",
        ],
    },
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
requests>=2.25.1
pandas>=1.2.0
numpy>=1.19.0
pytest>=6.0.0
black>=20.8b1
flake8>=3.9.0
"""

# TODO: README.md
"""
# My Package

A short description of your package.

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package import core

result = core.process_data("input")
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

MIT License
"""

# TODO: LICENSE
"""
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
include LICENSE
include README.md
include requirements.txt
recursive-include docs *
recursive-exclude tests *
"""

# TODO: __init__.py
"""
"""
from .core import process_data
from .utils import helper_function

__version__ = "0.1.0"
__author__ = "Your Name"
"""

# TODO: core.py
"""
def process_data(input_data: str) -> str:
    \"\"\"
    Process input data.

    Args:
        input_data (str): Input data to process.

    Returns:
        str: Processed data.
    \"\"\"
    return input_data.upper()
"""

# TODO: utils.py
"""
def helper_function() -> str:
    \"\"\"
    A helper function.

    Returns:
        str: A helpful message.
    \"\"\"
    return "I'm helping!"
"""

# TODO: test_core.py
"""
import pytest
from my_package.core import process_data

def test_process_data():
    assert process_data("test") == "TEST"
"""

# TODO: conf.py
"""
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

# TODO: index.rst
"""
Welcome to My Package's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/core
   modules/utils

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
    # Create package structure
    os.makedirs("my_package/my_package/tests", exist_ok=True)
    os.makedirs("my_package/docs", exist_ok=True)
    
    # Create files
    with open("my_package/setup.py", "w") as f:
        f.write('''
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
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.9.0",
        ],
    },
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
''')
    
    with open("my_package/requirements.txt", "w") as f:
        f.write('''
requests>=2.25.1
pandas>=1.2.0
numpy>=1.19.0
pytest>=6.0.0
black>=20.8b1
flake8>=3.9.0
''')
    
    with open("my_package/README.md", "w") as f:
        f.write('''
# My Package

A short description of your package.

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package import core

result = core.process_data("input")
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

MIT License
''')
    
    with open("my_package/LICENSE", "w") as f:
        f.write('''
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
''')
    
    with open("my_package/MANIFEST.in", "w") as f:
        f.write('''
include LICENSE
include README.md
include requirements.txt
recursive-include docs *
recursive-exclude tests *
''')
    
    with open("my_package/my_package/__init__.py", "w") as f:
        f.write('''
from .core import process_data
from .utils import helper_function

__version__ = "0.1.0"
__author__ = "Your Name"
''')
    
    with open("my_package/my_package/core.py", "w") as f:
        f.write('''
def process_data(input_data: str) -> str:
    """
    Process input data.

    Args:
        input_data (str): Input data to process.

    Returns:
        str: Processed data.
    """
    return input_data.upper()
''')
    
    with open("my_package/my_package/utils.py", "w") as f:
        f.write('''
def helper_function() -> str:
    """
    A helper function.

    Returns:
        str: A helpful message.
    """
    return "I'm helping!"
''')
    
    with open("my_package/my_package/tests/test_core.py", "w") as f:
        f.write('''
import pytest
from my_package.core import process_data

def test_process_data():
    assert process_data("test") == "TEST"
''')
    
    with open("my_package/docs/conf.py", "w") as f:
        f.write('''
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
''')
    
    with open("my_package/docs/index.rst", "w") as f:
        f.write('''
Welcome to My Package's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/core
   modules/utils

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
''')
    
    print("Package structure created successfully!")

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