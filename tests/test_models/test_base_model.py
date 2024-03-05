#!/usr/bin/python3
"""unittest for base_model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class"""
    def test_init_without_arguments(self):
        """Test the __init__ method without arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))
    
    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_UniqId(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()