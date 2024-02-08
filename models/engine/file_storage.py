"""File storage module.
This module provides file storage functionality for
the AirBnB
T"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This module provides file storage and
 that serializes instances to a JSON file
 and deserializes JSON file to instances:"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __object"""
        return self.__objects

    def new(self, obj):
        """Adds new instance to __object with
        key <obj class name>.id"""
        newObj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(newObj, obj.id)] = obj

    def save(self):
        """serializes __objects to the J
        SON file (path: __file_path)
        """
        _dict = FileStorage.__objects
        _objectDic = {obj: _dict[obj].to_dict() for obj in _dict.keys()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(_objectDic, file)

    def reload(self):
        """Reloads the __objects dictionary.
        deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                _dict = json.load(file)
                for obj in _dict.values():
                    _className = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(_className)(**obj))
        except FileNotFoundError:
            return
