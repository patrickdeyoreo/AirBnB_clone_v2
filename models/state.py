#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: relationship to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', back_populates='state', cascade='all, delete-orphan'
    )
