#!/usr/bin/python3
"""unittest for base_model"""
import unittest
import time
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

    def test_IfBadIdInArg(self):
        model1 = BaseModel()
        try:
            model2 = BaseModel(id= model1.id)
        except TypeError:
            self.fail("BaseModel raised TypeError unexpectedly!")


    def test_init_with_arguments(self):
        my_model = BaseModel(id='123', created_at='2022-01-01T00:00:00',
                             updated_at='2022-01-01T00:00:00')
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.created_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))
        self.assertEqual(my_model.updated_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.001)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

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


if __name__ == '__main__':
    unittest.main()