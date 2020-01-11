import os
import sys
from os.path import abspath, dirname, join
from unittest import defaultTestLoader, TextTestRunner


CURDIR = dirname(abspath(__file__))


def run_unit_tests():
    sys.path.insert(0, join(CURDIR, os.pardir, 'pageobject'))
    try:
        suite = defaultTestLoader.discover(join(CURDIR, 'utest'), 'test_*.py')
        result = TextTestRunner().run(suite)
    finally:
        sys.path.pop(0)
    return min(len(result.failures) + len(result.errors), 255)


if __name__ == '__main__':
    sys.exit(run_unit_tests())
