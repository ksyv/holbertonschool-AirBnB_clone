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


if __name__ == '__main__':
    unittest.main()
