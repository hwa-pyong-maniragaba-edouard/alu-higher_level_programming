#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 10, 4]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_negatives_and_positives(self):
        self.assertEqual(max_integer([-5, 0, 5, -10]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_all_zeros(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**20, 5, 10**19]), 10**20)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[1, 2], [3], [0]]), [3])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_argument(self):
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])


if __name__ == '__main__':
    unittest.main()
