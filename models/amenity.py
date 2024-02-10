#!/usr/bin/python3
from models.base_model import BaseModel
 
class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        #initializes Amenity class
        super().__init__(*args, **kwargs)
        self.name = ''

