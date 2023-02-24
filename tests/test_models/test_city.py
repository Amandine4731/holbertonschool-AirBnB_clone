#!/usr/bin.python3
"""
    Module of Unittests for models/city.py

"""

import unittest
from models.base_model import BaseModel
from models.city import City
import os
from datetime import datetime
import models
from unittest.mock import patch
import uuid

class Test_City(unittest.TestCase):
    """
        Tests of the subclass City, it inherit from BaseModel.
    """

    def test_NameAttribut(self):
        c1 = City(name="Toulouse")
        # test value of attribut
        self.assertEqual(c1.name, "Toulouse")

    def test_AttbStr(self):
        """ checks city's attributes """
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))

    def test_CityDict(self):
        created_at = datetime.now()
        created_at = created_at.isoformat()
        updated_at = datetime.now()
        updated_at = updated_at.isoformat()
        c1 = City(name="Toulouse", id=uuid.uuid4(), created_at=created_at, updated_at= updated_at)
        d = c1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['__class__'], 'City')
        self.assertEqual(d['name'], 'Toulouse')