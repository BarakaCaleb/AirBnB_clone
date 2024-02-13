#!/usr/bin/python3

"""__init__ the magic method for directory models"""

from models.engine.file_storage import Filestorage


storage = Filestorage()
storage.reload()
