#!/usr/bin/python3
"""Amenity Class that Inherrits the BaseModel class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class that Inherits the BaseModel class
    Attributes:
        name (str): Name of the Amenity
    """

    name = ""
