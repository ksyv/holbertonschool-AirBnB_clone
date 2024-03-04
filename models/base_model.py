#!/usr/bin/python3
"""This modul contain the base class for all models"""
# this is the base class of all our models
import uuid
from datetime import datetime


class BaseModel:
    """Base class who contain:
    Attributes:
        - id
        - created at
        - updates_at
    Methods:
        - save()
        - to_json()"""
    def __init__(self, *args, **kwargs):
        """init instance attributes"""
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                if key == "created_at":
                    value = value.isoformat()
                elif key == "updated_at":
                    value = value.isoformat()
                else:
                    setattr(self, key, value)

    def __str__(self):
        """define the string representation of class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance, datetime in iso format"""
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at":
                dictionary[key] = value.isoformat()
            elif key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
