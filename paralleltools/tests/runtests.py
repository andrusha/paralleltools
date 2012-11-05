#!/usr/bin/env python

import os
import sys
import unittest

sys.path.insert(0,
    os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from tests.acceptance_tests import AcceptanceTestCase


def main():
    tests = suite()
    unittest.TextTestRunner(verbosity=2).run(tests)


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AcceptanceTestCase))
    return tests

if __name__ == "__main__":
    main()
