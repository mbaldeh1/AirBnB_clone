#!/usr/bin/python3

"""
This Initializes Module Global Variables (Singleton)
"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
