#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        # initializes user class
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
