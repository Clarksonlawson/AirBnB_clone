#!/usr/bin/python3
"""Review Class that Models the User Reviews
and inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that Models the User Reviews
    Attributes:
    place_id (str): The id of the reviewed place
    user_id (str): The id of the User reviewing the place
    text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
