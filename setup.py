import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.version_info <= (2, 5):
    error = "ERROR: paralleltools requires Python Version 2.6 or above...exiting."
    print >> sys.stderr, error
    sys.exit(1)

setup(
    name="paralleltools",
    version="0.0.1",
    author="Andrew Korzhuev",
    author_email="korzhuev@andrusha.me",
    description=("A collection of basic list functions which can be run "
                 "in parallel mode (both sync or async)."),
    license="MIT",
    keywords="parallel threading map filter reduce async",
    url="http://github.com/andrusha/paralleltools",
    packages=['paralleltools', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
