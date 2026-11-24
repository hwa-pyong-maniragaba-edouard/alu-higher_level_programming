#!/usr/bin/python3
"""Unittests for create, save_to_file and load_from_file."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestFiles(unittest.TestCase):
    """Test cases for create, save_to_file and load_from_file."""

    def setUp(self):
        Base._Base__nb_objects = 0
        self.remove_files()

    def tearDown(self):
        self.remove_files()

    @staticmethod
    def remove_files():
        for name in ("Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    @staticmethod
    def read(name):
        with open(name, "r", encoding="utf-8") as f:
            return f.read()

    def test_rectangle_create(self):
        for d in ({"id": 89}, {"id": 89, "width": 1},
                  {"id": 89, "width": 1, "height": 2},
                  {"id": 89, "width": 1, "height": 2, "x": 3},
                  {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}):
            r = Rectangle.create(**d)
            self.assertIsInstance(r, Rectangle)
            for key, value in d.items():
                self.assertEqual(getattr(r, key), value)

    def test_square_create(self):
        for d in ({"id": 89}, {"id": 89, "size": 1},
                  {"id": 89, "size": 1, "x": 2},
                  {"id": 89, "size": 1, "x": 2, "y": 3}):
            s = Square.create(**d)
            self.assertIsInstance(s, Square)
            for key, value in d.items():
                self.assertEqual(getattr(s, key), value)

    def test_rectangle_save_none(self):
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_rectangle_save_empty(self):
        Rectangle.save_to_file([])
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_rectangle_save_one(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        data = json.loads(self.read("Rectangle.json"))
        self.assertEqual(
            data, [{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}])

    def test_square_save_none(self):
        Square.save_to_file(None)
        self.assertEqual(self.read("Square.json"), "[]")

    def test_square_save_empty(self):
        Square.save_to_file([])
        self.assertEqual(self.read("Square.json"), "[]")

    def test_square_save_one(self):
        Square.save_to_file([Square(1)])
        data = json.loads(self.read("Square.json"))
        self.assertEqual(data, [{"id": 1, "size": 1, "x": 0, "y": 0}])

    def test_rectangle_load_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIsNot(loaded[0], r1)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_square_load_no_file(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIsNot(loaded[0], s1)
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), s2.to_dictionary())


if __name__ == '__main__':
    unittest.main()
