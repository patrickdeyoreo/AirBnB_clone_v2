#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import models
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine import db_storage, file_storage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()

storage.reload()
