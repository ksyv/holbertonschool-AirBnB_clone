#!/usr/bin/python3
""" Modul for test the Amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenityClass(unittest.TestCase):
    """Unittest for Amenity class"""
    def test_inheritance(self):
        AmenityTest = Amenity()
        self.assertIsInstance(AmenityTest, BaseModel)

    def test_nameAttribute(self):
        AmenityTest = Amenity()
        self.assertEqual(AmenityTest.name, "")
        self.assertIsInstance(AmenityTest.name, str)


if __name__ == '__main__':
    unittest.main()
