#!/usr/bin/python3
"""This is the city class"""
from models.base_model import Base, BaseModel
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
        state: relationship between a state and cities
        places: relationship between a city and places
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship(
        'State', back_populates='cities'
    )
    places = relationship(
        'Place', back_populates='cities', cascade='all, delete-orphan'
    )
