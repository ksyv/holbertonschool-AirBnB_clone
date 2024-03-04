#!/usr/bin/python3
"""This modul contain the base class for all models"""
# this is the base class of all our models
import uuid


class BaseModel:
    """Base class who contain:
    Attributes:
        - id
        - created at
        - updates_at
    Methods:
        - save()
        - to_json()"""
    