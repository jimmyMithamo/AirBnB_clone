#!/usr/bin/python3
"""state class"""
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        # initializes user class
        super().__init__(*args, **kwargs)
        self.name = ''
