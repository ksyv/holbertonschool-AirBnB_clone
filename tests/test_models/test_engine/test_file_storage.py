#!/usr/bin/python3
"""unittest for file_storage"""
import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test case for the FileStorage class"""
    def test_Storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorageWithoutArgs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorageWithArg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorageFilePath(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorageObject(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_new(self):
        """Test the 'new' method of the storage object."""
        storage = FileStorage()
        new_model = BaseModel()
        storage.new(new_model)
        all_objs = storage.all()
        self.assertIn(f"{new_model.__class__.__name__}.{new_model.id}",
                      all_objs)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        self.base_model = BaseModel()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        self.assertIn(f"{self.base_model.__class__.__name__}.{self.base_model.id}", all_objs)

if __name__ == '__main__':
    unittest.main()
