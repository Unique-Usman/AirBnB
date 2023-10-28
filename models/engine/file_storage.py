#!/usr/bin/python3
"""This module contains the FileStorage class
which handles the serialization and deserialization
of the instances of BaseModel class in using json format
for the project"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place

class FileStorage():
    """The class for handling file storage

    It handles the serilization of the instances to JSON file
    and the deserialization of the JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the class attribure __objects

        Returns:
            dict: the dictionary that stores all objects
        """

        return FileStorage.__objects

    def new(self, obj) -> None:
        """For adding new object instances

        Args:
            obj: the object to store
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """To save all the object in the class to a json file

        Serialize all the object to a JSON file
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(objdict, fd)

    def reload(self) -> None:
        """To deserialized the JSON file

        deserialized the JSON file to __objects if the __file_path
        exist else do nothing and no exception should be raised
        """
        try:
            with open(FileStorage.__file_path) as fd:
                objdict = json.load(fd)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
