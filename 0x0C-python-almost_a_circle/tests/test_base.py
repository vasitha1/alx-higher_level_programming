#!/usr/bin/python3
"""
Unitest to test "Base" class
"""

import unittest
from model.base import Base

class TestBase(unittest.TestCase):

    def check_base_exists(self):
        """Method to check the existence of the Base class"""
        self.assertTrue('Base' in globals())

    def test_nb_objects_exist(self):
        """Method to test the existence of nb_objects"""
        self.assertTrue(hasattr(Base, 'nb_objects'))

    def test_global_attribut_init(self):
        """Method makes sure the "nb_objects" attribute is innitialised to 0"""
        self.assertEqual(_nb_objects, 0)

    def test_nb_objects_private(self):
        """Method to assert that nb object is private"""
        instance = Base()
        self.assertRaises(AttributeError):
            error = instance.__nb_objects

    def test_nb_objects_private_accessed(self):
        """Method to assert that nb can be accessed via private method"""
        instance = Base(2)
        self.assertEqual(instance.nb_objects(), 0)

class TestId(unittest.TestCase):
    def C
