#!/usr/bin/python2
"""
For creating the file storage or sqldatabase
instance to work with our website
"""
from os import getenv

# managing both storage using sqlalchemy and filestorage
if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
