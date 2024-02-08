#!/usr/bin/python3
"""Defines place models and inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place in the AirBnB database
    Attributes:
        name (str): The name of the place
        description (str): The description of the place
        city_id (int): The city id of the place
        user_id (int): The user id of the User
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest(int): The maximum number of guests
        price_by_night (int): The price of the room per night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): The amenity ids of the place
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
