"""
cite
"""

import versioneer
import os

from setuptools import setup

path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(path, "README.md"), "r") as f:
    readme = f.read()

cmdclass = versioneer.get_cmdclass()

setup(
    name="cite",
    version=versioneer.get_version(),
    description="Command line tool to turn DOIs into citations",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Robert Gieseke",
    author_email="rob.g@web.de",
    url="https://github.com/rgieseke/cite",
    license="BSD",
    keywords=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cite"],
    cmdclass=cmdclass,
    install_requires=["requests", "lxml", "python-slugify[unidecode]"],
    entry_points={"console_scripts": ["cite=cite:main"]},
)
