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

    def save(self):
        """serializes __objects to the JSON file with path __file_path"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, file)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                instance = json.load(file)
                for key, value in instance.items():
                    self.__obj[key] = value
        except FileNotFoundError:
            pass
