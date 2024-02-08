#!/usr/bin/python3

"""Basemodel class for all models.
    defines all common attributes/methods for other classes
"""
import uuid
import datetime
import models

class BaseModel:
    """
        Base class for all models
         defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel with values"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the model"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model"""
        inst_dic = self.__dict__.copy()
        inst_dic["__class__"] = self.__class__.__name__
        inst_dic["created_at"] = self.created_at.isoformat()
        inst_dic["updated_at"] = self.updated_at.isoformat()
        return inst_dic
