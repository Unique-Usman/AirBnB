#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
"""The state class which represent the BaseModel class"""

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", 
                            backref="state", cascade="all, delete, delete-orphan")
    else:
        name = ''
        @property
        def cities(self):
            """Getter for cities property."""
            from models import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
