#!/usr/bin/python3
"""unittest for base_model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.Testcase):
    """Test case for the BaseModel class"""
    def test_init_without_arguments(self):
        """Test the __init__ method without arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))


if __name__ == '__main__':
    unittest.main()