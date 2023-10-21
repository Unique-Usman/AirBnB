#!/usr/bin/python3
"""This module contains the FileStorage class
which handles the serialization and deserialization
of the instances of BaseModel class in using json format
for the project"""
import json

class FileStorage():
    """The class for handling file storage

    It handles the serilization of the instances to JSON file
    and the deserialization of the JSON file to instances
    """

    __file_path = ="file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the class attribure __objects
        
        Returns:
            dict: the dictionary that stores all objects
        """

        return FileStorage.__objects
    
    def new(self, obj) ->None:
        """For adding new object instances
        
        Args:
            obj: the object to store 
        """
        FileStorage.__objects[f"{obj.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """To save all the object in the class to a json file
        
        Serialize all the object to a JSON file
        """
        with open(f"{FileStorage.__file_path}", "w", encoding="UTF-8") as fd:
            json.dump(FileStorage.all(), fd)

    def reload(self) -> None:
        """To deserialized the JSON file
        
        deserialized the JSON file to __objects if the __file_path
        exist else do nothing and no exception should be raised
        """
        try:
            with open(f"{FileStorage.__file_path}", "r", encoding="UTF-8") as fd:
                FileStorage.__file_path = json.load(fd)
        except Exception as e:
            pass
