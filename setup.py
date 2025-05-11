#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup

from wagtail_wordpress_import import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "docs/long_description.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtail-wordpress-import",
    version=__version__,
    description="Import XML data into wagtail to create pages and content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nick Moreton",
    author_email="nickmoreton@me.com",
    url="https://github.com/torchbox/wagtail-wordpress-import",
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 6",
        "Framework :: Wagtail :: 7",
    ],
    install_requires=[
        "Django>=4.2",
        "Wagtail>=6.3",
        "lxml>=5.3.0,<5.4",
        "bleach>=4.1.0,<5",
        "prettytable>=3.16.0,<4",
        "shortcodes>=5.4.0,<6",
        "cached-property>=2.0.1,<3",
        "html5lib>=1.1,<2",
    ],
    extras_require={
        "testing": [
            "freezegun==1.5.1",
            "responses==0.25.7",
            "flake8==7.2.0",
            "isort==6.0.1",
            "black==25.1.0",
        ],
    },
    zip_safe=False,
)
