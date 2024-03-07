#!/usr/bin/python3
""" Modul for test the place class"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlaceClass(unittest.TestCase):
    """Unittest for Place class"""
    def test_inheritance(self):
        placeTest = Place()
        self.assertIsInstance(placeTest, BaseModel)

    def test_city_idAttribute(self):
        placeTest = Place()
        self.assertEqual(placeTest.city_id, "")
        self.assertIsInstance(placeTest.city_id, str)

    def test_user_idAttribute(self):
        placeTest = Place()
        self.assertEqual(placeTest.user_id, "")
        self.assertIsInstance(placeTest.user_id, str)

    def test_nameAttribute(self):
        placeTest = Place()
        self.assertEqual(placeTest.name, "")
        self.assertIsInstance(placeTest.name, str)

    def test_descriptionAttribute(self):
        placeTest = Place()
        self.assertEqual(placeTest.description, "")
        self.assertIsInstance(placeTest.description, str)


if __name__ == '__main__':
    unittest.main()