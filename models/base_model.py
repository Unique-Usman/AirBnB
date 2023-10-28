#!usr/bin/python3
import uuid
from datetime import datetime
import models

# This module  which define base class for all the subclass
# in this Airbnb Project. Other classes are
# User, State, City and Place.


class BaseModel():
    """This the base class for other class

    Other classed like the User, State, City and Place
    Inherit from the base class. It defines Instance
    Like id, created_at, updated_at etc.
    """

    def __init__(self, *args, **kwargs) -> None:
        """To initialize the BaseModel Class

        If the args or kwargs is present and not empty then, the instance initialization
        is done with either of the args of kwargs, while if it is empty, the initialization
        is done by randomly generating the value for those instance using
        datetime module and uuid module.

        Args:
            args (tuple): list representation of an instance i.e it attributes
            kwargs (dict): dict representation of an instance i.e it attributes
        """

        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)
        else:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs.get(key))

    def __str__(self) -> str:
        """It return the string representation of the Obj of the Class

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """It returns the dict representation of the class

        Args:
            dict: The dictionary representation of the class
        """
        rdic = self.__dict__.copy()
        rdic["__class__"] = self.__class__.__name__
        rdic["updated_at"] = self.updated_at.isoformat(sep='T', timespec='microseconds')
        rdic["created_at"] = self.created_at.isoformat(sep='T', timespec='microseconds')
        return rdic
