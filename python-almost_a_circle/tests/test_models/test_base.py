#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_given(self):
        self.assertEqual(Base(12).id, 12)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_dict(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{'id': 89}])

    def test_from_json_string_returns_list(self):
        self.assertEqual(type(Base.from_json_string('[{ "id": 89 }]')), list)


if __name__ == '__main__':
    unittest.main()
