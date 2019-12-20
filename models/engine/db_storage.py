#!/usr/bin/python3
"""This is a DBStorage class for Airbnb"""
import json
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """class"""
    __engine = None
    __session = None

    def __init__(self):
        """Connect to a database and initiate a session"""
        url = {
            'drivername': 'mysql+mysqldb',
            'username': getenv('HBNB_MYSQL_USER'),
            'password': getenv('HBNB_MYSQL_PWD'),
            'host': getenv('HBNB_MYSQL_HOST'),
            'port': getenv('HBNB_MYSQL_PORT'),
            'database': getenv('HBNB_MYSQL_DB'),
        }
        self.__engine = create_engine(URL(**url), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Get a dictionary of all objects
        Return:
            returns a dictionary of objects
        """
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for res in map(self.__session.query, classes)
                    for obj in res.all()}
        else:
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for obj in self.__session.query(cls).all()}

    def new(self, obj):
        """sets __session to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """SOME COMMENT
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from __session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """INCOMPLETE serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
