import re

from setuptools import find_packages, setup

from aider import __version__

setup(
    name="aider-benchmark",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    description="aider is GPT powered coding in your terminal",
    long_description_content_type="text/markdown",
    url="https://github.com/paul-gauthier/aider",
)
