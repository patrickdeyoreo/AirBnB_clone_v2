"""incomplete edit"""

#!/usr/bin/python3
"""This is a DBStorage class for Airbnb"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """class"""
    __engine = None
    __session = None
    
    __init__(self):
        """INCOMPLETE"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                getenv(''),
        )pool_pre_ping=True)
        if getenv(HBNB_ENV) == 'test'
      
    def all(self, cls=None):
        """INCOMPLETE returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            return [obj for obj in self.__objects if type(obj) is cls]

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

    def reload(self):
        """INCOMPLETE serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __session
        """
        if obj:
            self.__session.delete(obj)