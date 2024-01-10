#/usr/bin/bash
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship
from os import getenv

"""Amenity module which contains the amenity class"""


storage_type = getenv("HBNB_TYPE_STORAGE")
class Amenity(BaseModel, Base):
    """The amenity class"""

    __tablename__ = "amenities"

    if storage_type == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
