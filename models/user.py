#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from models.place import Place
from models.city import City

"""The user class that inherit from the BaseModel

The user class represents the User of the AirBnB
"""

storage_type = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """User class which inherit from BaseModel"""
    
    __tablename__ = "users"

    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", 
                            backref="user", cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
