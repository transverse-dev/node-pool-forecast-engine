#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description="Describe Your Cool Project",
    author="Jonghyeon Ham",
    author_email="kidevelop@transverse.ai",
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url="https://github.com/transverse-dev/node-pool-forecast-engine",
    install_requires=["pytorch-lightning", "hydra-core"],
    packages=find_packages(),
)
