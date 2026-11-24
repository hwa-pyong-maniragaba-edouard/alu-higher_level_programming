#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_one_arg(self):
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 0, 0, 1))
        self.assertEqual((s.width, s.height), (1, 1))

    def test_two_args(self):
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_four_args(self):
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_size_setter(self):
        s = Square(1)
        s.size = 5
        self.assertEqual((s.width, s.height), (5, 5))

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_str(self):
        self.assertEqual(str(Square(5, 2, 3, 12)), "[Square] (12) 2/3 - 5")
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_display(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            Square(2, 1, 1).display()
        self.assertEqual(out.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 7)
        self.assertEqual(s.to_dictionary(),
                         {"id": 7, "size": 10, "x": 2, "y": 1})

    def test_update_no_args(self):
        s = Square(5, 1, 2, 3)
        s.update()
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_args(self):
        s = Square(5, 1, 2, 3)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 5")
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 1")
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/2 - 1")
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwargs(self):
        s = Square(5, 1, 2, 3)
        s.update(id=89)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 5")
        s.update(id=89, size=1)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 1")
        s.update(id=89, size=1, x=2)
        self.assertEqual(str(s), "[Square] (89) 2/2 - 1")
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_args_before_kwargs(self):
        s = Square(5, 1, 2, 3)
        s.update(89, 2, size=9)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 2")

    def test_update_invalid(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "2")


if __name__ == '__main__':
    unittest.main()
