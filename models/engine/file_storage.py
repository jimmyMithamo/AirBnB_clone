import os
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

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

        
        with open (self.__file_path, 'w', encoding = 'utf-8') as file:
            json.dump(serialized_objects, file, indent = 4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        if os.path.exists(self.__file_path):
            try:
                with open (self.__file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                pass

    
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                if class_name in globals():
                    class_obj = self.__class__mapping[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj
