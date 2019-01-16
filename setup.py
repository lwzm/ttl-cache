#!/usr/bin/env python

from setuptools import setup

name = "ttl-cache"
author = "lwzm"

with open("README.md") as f:
    long_description = f.read()


setup(
    name=name,
    version="1.4",
    description="Decorator to wrap a function with a memoizing callable that has TTL result",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email="{}@qq.com".format(author),
    keywords="cache ttl decorator functools".split(),
    url="https://github.com/{}/{}".format(author, name),
    py_modules=["ttl_cache"],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
