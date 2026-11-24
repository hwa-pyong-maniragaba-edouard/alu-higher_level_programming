#!/usr/bin/python3
"""Unittests for the Rectangle methods."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Test cases for Rectangle methods."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_id(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_no_x_no_y(self):
        r = Rectangle(4, 6)
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
        self.assertEqual(out.getvalue(), "####\n" * 6)

    def test_display_no_y(self):
        r = Rectangle(2, 2, 2)
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
        self.assertEqual(out.getvalue(), "  ##\n  ##\n")

    def test_display_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        with patch("sys.stdout", new=io.StringIO()) as out:
            r.display()
        self.assertEqual(out.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_height(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_x(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_y(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_before_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, height=5)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_invalid(self):
        r = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 2, 0)


if __name__ == '__main__':
    unittest.main()
