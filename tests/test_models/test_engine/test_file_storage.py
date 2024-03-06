#!/usr/bin/python3
"""unittest for file_storage"""
import unittest
import json
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime  # Ajout de l'importation manquante

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
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model_data = {
            "__class__": "BaseModel",
            "id": "test_id",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T01:00:00",
        }

    @classmethod
    def tearDown(self):
        try:
           os.remove("file.json")
        except FileNotFoundError:
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

    def test_reload_with_existing_file(self):
        """Test reload when the file exists"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({"BaseModel.test_id": self.base_model_data}, file)

        self.storage.reload()

        objects = self.storage.all()
        self.assertIn("BaseModel.test_id", objects)
        reloaded_instance = objects["BaseModel.test_id"]

        # Assert that the reloaded instance is of the correct type
        self.assertIsInstance(reloaded_instance, BaseModel)

        # Assert that the attributes of the reloaded instance match the expected values
        self.assertEqual(reloaded_instance.id, "test_id")
        self.assertEqual(reloaded_instance.created_at, datetime.fromisoformat("2022-01-01T00:00:00"))
        self.assertEqual(reloaded_instance.updated_at, datetime.fromisoformat("2022-01-01T01:00:00"))

    def test_reload_with_nonexistent_file(self):
        """Test reload when the file does not exist"""
        self.storage.reload()

        # Assert that the storage remains empty when the file does not exist
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

if __name__ == '__main__':
    unittest.main()
