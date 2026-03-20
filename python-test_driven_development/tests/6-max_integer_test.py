#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test list with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_numbers(self):
        """Test list with mixed integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_max(self):
        """Test when max is in middle."""
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)

    def test_last_max(self):
        """Test when max is last."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_float_numbers(self):
        """Test list with floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_same_values(self):
        """Test list with identical values."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_string_list(self):
        """Test list with strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        