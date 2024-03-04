#!/usr/bin/python3
"""This modul contain the base class for all models"""
# this is the base class of all our models
import uuid
from datetime import date, datetime


class BaseModel:
    """Base class who contain:
    Attributes:
        - id
        - created at
        - updates_at
    Methods:
        - save()
        - to_json()"""
    def __init__(self):
        """init instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        return (f"[<class name>] (<self.id>) <self.__dict__>")
    
