#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))
        self.assertEqual(r.id, 1)

    def test_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_five_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
