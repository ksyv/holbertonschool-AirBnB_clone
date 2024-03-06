#!/usr/bin/python3
""" Modul for test the User class"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUserClass(unittest.TestCase):
    """Unittest for User class"""
    def test_inheritance(self):
        userTest = User()
        self.assertIsInstance(userTest, BaseModel)

    def test_emailAttribute(self):
        userTest = User()
        self.assertEqual(userTest.email, "")
        self.assertIsInstance(userTest.email, str)

    def test_passwordAttribute(self):
        userTest = User()
        self.assertEqual(userTest.password, "")
        self.assertIsInstance(userTest.password, str)

    def test_first_nameAttribute(self):
        userTest = User()
        self.assertEqual(userTest.first_name, "")
        self.assertIsInstance(userTest.first_name, str)

    def test_last_nameAttribute(self):
        userTest = User()
        self.assertEqual(userTest.last_name, "")
        self.assertIsInstance(userTest.last_name, str)


if __name__ == '__main__':
    unittest.main()
