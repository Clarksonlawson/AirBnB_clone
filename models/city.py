#!/usr/bin/python3
"""City Class that inherits from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class that inherits from the BaseModel
    Attributes:
        name (str): City name
        state_id (str): City state id
    """

    state_id = ""
    name = ""
