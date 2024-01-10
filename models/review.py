#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
"""The class for reviews"""

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """The review class"""

    __tablename__ = "reviews"
    if storage_type == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
