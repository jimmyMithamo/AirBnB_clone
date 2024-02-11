#!/usr/bin/python3
import os
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    __class_mapping = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        if os.path.exists(self.__file_path):
           with open(self.__file_path, 'r', encoding='utf-8') as file:
              try:
                  serialized_objects = json.load(file)
                  for key, value in serialized_objects.items():
                      class_name, obj_id = key.split('.')

                      cls = globals()[class_name]

                      instance = cls.load_from_dict(value)

                      self.__objects[key] = instance
              except FileNotFoundError:
                  pass
                  """" print"""

            """for key, value in data.items():
                class_name, obj_id = key.split('.')
                try:
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj
                except NameError:
                    pass
                """"""
                if class_name in globals():
                    class_obj = self.__class_mapping[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj"""
