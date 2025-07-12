#!/usr/bin/env python3
"""
Setup script for Ethical Hacking 2030
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="ethical_hacking_2030",
    version="0.1.0",
    author="Ethical Hacking 2030 Team",
    author_email="your.email@example.com",
    description="A comprehensive ethical hacking framework for 2030",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Ethical_Hacking_2030",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Networking",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ethical-hacking=ethical_hacking_2030.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "ethical_hacking_2030": [
            "data/*",
            "config/*",
            "templates/*",
        ],
    },
    zip_safe=False,
) 