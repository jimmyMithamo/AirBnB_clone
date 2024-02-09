#!/usr/bin/python3
import uuid

from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            # if kwargs is not empty,recreate an instance from dictionary
            for key, value in kwargs.items():
                if key == '__class__':
                    continue # skip __class__attribute
                if key in ('created_at', 'updated_at'):
                    # convert strings to datetime objects
                    if not isinstance(value, datetime):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            # if kwargs is empty create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            """
            register the instance in the __objects
            """

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id,self.__dict__)

    def save(self):
        from models import storage
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
        #storage.new(self)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
    """

        return {
                "__class__": self.__class__.__name__,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                **self.__dict__ #include othe object attributes
                }
                """
