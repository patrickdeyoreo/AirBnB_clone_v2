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
        env = getenv('HBNB_ENV', 'dev')
        url = {
            'drivername': 'mysql+mysqldb',
            'username': getenv('HBNB_MYSQL_USER', 'hbnb_{}'.format(env)),
            'password': getenv('HBNB_MYSQL_PWD', 'hbnb_{}_pwd'.format(env)),
            'host': getenv('HBNB_MYSQL_HOST', 'localhost'),
            'port': getenv('HBNB_MYSQL_PORT', 3306),
            'database': getenv('HBNB_MYSQL_DB', 'hbnb_{}_db'.format(env)),
        }
        self.__engine = create_engine(URL(**url), pool_pre_ping=True)
        self.reload()

    def all(self, cls=None):
        """
        Get a dictionary of all objects
        Return:
            returns a dictionary of objects
        """
        if cls is None:
            results = self.__session.query(
                User, State, City, Amenity, Place, Review
            ).all()
        else:
            results = self.__session.query(cls).all()
        return {
            '.'.join([type(obj).__name__, obj.id]): obj for obj in results
        }

    def new(self, obj):
        """sets __session to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """SOME COMMENT
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from __session
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """INCOMPLETE serialize the file path to JSON file path
        """
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
