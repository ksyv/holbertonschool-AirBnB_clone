#!/usr/bin/python3
""" Modul for test the City class"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCityClass(unittest.TestCase):
    """Unittest for City class"""
    def test_inheritance(self):
        CityTest = City()
        self.assertIsInstance(CityTest, BaseModel)

    def test_state_idAttribute(self):
        CityTest = City()
        self.assertEqual(CityTest.state_id, "")
        self.assertIsInstance(CityTest.state_id, str)

    def test_nameAttribute(self):
        CityTest = City()
        self.assertEqual(CityTest.name, "")
        self.assertIsInstance(CityTest.name, str)


if __name__ == '__main__':
    unittest.main()
