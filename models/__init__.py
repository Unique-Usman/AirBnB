#!/usr/bin/python3
"""
For creating the file storage instance to work with our website
"""
from models.engine.file_storage import FileStorage

# storage, an instance of FileStorage
storage = FileStorage()
storage.reload()
