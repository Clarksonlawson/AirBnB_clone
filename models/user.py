#!/usr/bin/python3
"""User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel
    Attributes:
        email (str): User email
        password (str): <PASSWORD>
        first_name (str): User first name
        last_name (str): User last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
