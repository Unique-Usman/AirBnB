#!usr/bin/python3
import uuid
from datetime import datetime

# This module define base class for all the subclass
# in this Airbnb Project. Other classes are
# User, State, City and Place. 


class BaseModel():
    """This the base class for other class

    Other classed like the User, State, City and Place
    Inherit from the base class. It defines Instance
    Like id, created_at, updated_at etc.
    """

    def __init__(self) -> None:
        """To initialize the BaseModel Class"""
        self.id = str(uuid.uuid4())
        current_time = datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def __str__(self) -> str:
        """It return the string representation of the Obj of the Class

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute updated_at with current datetime"""

        current_time = datetime.now().isoformat(sep="T", timespec="microseconds")
        self.updated_at = current_time

    def to_dict(self) -> dict:
        """It returns the dict representation of the class

        Args:
            dict: The dictionary representation of the class
        """
        self.__dict__["__class__"] = f"{self.__class__.__name__}"
        self.updated_at = f"{self.updated_at}"
        self.created_at = f"{self.created_at}"
        return self.__dict__
