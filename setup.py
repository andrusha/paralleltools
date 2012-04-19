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
    version="0.0.2",
    author="Andrew Korzhuev",
    author_email="korzhuev@andrusha.me",
    description=("A collection of basic list functions which can be run "
                 "in parallel mode (both sync or async)."),
    long_description=read('README.md').split('=====')[2][:-6].strip(),
    keywords="parallel threading map filter reduce async",
    license='MIT',
    url="http://github.com/andrusha/paralleltools",
    packages=['paralleltools'],
    test_suite='tests.runtests',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
