#!/usr/bin/python3
"""
0x00. AirBnb clone - The console
Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines attributes/methods for the Place class, subclass of BasModel
    Other attributes/methods are inherited from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
