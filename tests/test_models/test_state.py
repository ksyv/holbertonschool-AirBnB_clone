#!/usr/bin/python3
""" Modul for test the State class"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestStateClass(unittest.TestCase):
    """Unittest for State class"""
    def test_inheritance(self):
        StateTest = State()
        self.assertIsInstance(StateTest, BaseModel)

    def test_nameAttribute(self):
        StateTest = State()
        self.assertEqual(StateTest.name, "")
        self.assertIsInstance(StateTest.name, str)


if __name__ == '__main__':
    unittest.main()
