#!/usr/bin/python3
"""defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents the city.
    Attributes:
    state_id(str): state id
    name (str): name of city
    """
    state_id = ""
    name = ""
