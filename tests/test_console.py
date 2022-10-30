#!/usr/bin/python3
"""
Module: test_console
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):

    def setUp(self):
        """ setting requirements needed to test"""
        with open("test.json", "w"):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}

    def tearDown(self):
        """ destroy files after test"""
        storage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass
