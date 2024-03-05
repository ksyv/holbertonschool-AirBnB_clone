#!/usr/bin/python3
"""modul for file storage"""
import json


class FileStorage(self):
    """serialize instances to a JSON file and deserialise JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    