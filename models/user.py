#!/usr/bin/python3
""" Modul for create the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User inherits from BaseModel with
    additional attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
