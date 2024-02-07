#!/usr/bin/python3
from models.engine.file_storage import FileStorage

"""create a unique FileStorage instance for the app"""
storage = FileStorage()

"""populating objects with the existing objects from the JSON file"""
storage.reload()
