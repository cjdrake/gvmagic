#!/usr/bin/env python
#
# Copyright 2016 Chris Drake
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

with open("VERSION") as fin:
    VERSION = fin.read().strip()

with open("README.rst") as fin:
    README = fin.read()

with open("LICENSE") as fin:
    LICENSE = fin.read()

URL = "https://github.com/cjdrake/gvmagic"

DOWNLOAD_URL = ""

CLASSIFIERS = [
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
]

setup(
    name="gvmagic",
    version=VERSION,
    author="Chris Drake",
    author_email="cjdrake@gmail.com",
    description="Graphviz IPython magic commands",
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    py_modules=["gvmagic"],
)
