#!/usr/bin/python3
"""Unittest for class BaseModel"""
import unittest
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """
    def test_init_with_arguments(self):
        """Test the __init__ method with valid arguments."""
        my_model = BaseModel(id='123', created_at='2022-01-01T00:00:00',
                             updated_at='2022-01-01T00:00:00')
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.created_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))
        self.assertEqual(my_model.updated_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))

    def test_str_empty_model(self):
        """Test the __str__ method with an empty model."""
        empty_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(empty_model.id,
                                                    empty_model.__dict__)
        self.assertEqual(str(empty_model), expected_str)

    def test_save_without_changes(self):
        """Test the save method without changes."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        time.sleep(0.001)  # Ensure the time has changed
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_with_additional_attributes(self):
        """Test the to_dict method with additional attributes."""
        my_model = BaseModel()
        my_model.name = 'John'
        my_model.age = 25
        expected_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            '__class__': 'BaseModel',
            'name': 'John',
            'age': 25
        }
        self.assertEqual(my_model.to_dict(), expected_dict)

    def test_init_with_invalid_id(self):
        """Test the __init__ method with an invalid id."""
        try:
            BaseModel(id=123)
        except TypeError:
            self.fail("BaseModel raised TypeError unexpectedly!")

    def test_str_with_missing_id(self):
        """Test the __str__ method with a missing id."""
        my_model = BaseModel()
        try:
            del my_model.id
            str(my_model)
        except AttributeError:
            pass

    def test_save_with_invalid_updated_at(self):
        """Test the save method with an invalid updated_at."""
        my_model = BaseModel()
        try:
            my_model.updated_at = '2022-01-01'
            my_model.save()
        except ValueError:
            self.fail("BaseModel raised ValueError unexpectedly!")

    def test_to_dict_with_reserved_attribute(self):
        """Test the to_dict method with a reserved attribute."""
        my_model = BaseModel()
        try:
            my_model.__class__ = 'InvalidClass'
            my_model.to_dict()
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()