#!/usr/bin/python3
"""modul for file storage"""
import json


class FileStorage():
    """serialize instances to a JSON file and deserialise JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary object"""
        return self.__object

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.name}.{obj.id}"
        self.__obj[key] = obj

