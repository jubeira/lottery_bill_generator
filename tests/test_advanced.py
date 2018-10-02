# -*- coding: utf-8 -*-

from .context import bill_generator

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(bill_generator.hmm())


if __name__ == '__main__':
    unittest.main()
