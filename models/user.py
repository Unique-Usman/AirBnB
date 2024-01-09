#!/usr/bin/python3
from models.base_model import BaseModel, Base

"""The user class that inherit from the BaseModel

The user class represents the User of the AirBnB
"""


class User(BaseModel, Base):
    """User class which inherit from BaseModel"""
    
    __tablename__ = "users"

    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
