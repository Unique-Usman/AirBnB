#!/usr/bin/python3
from models.city import City
import unittest
import models

"""Module for testing the City module(User class)"""

class TestCityClass(unittest.TestCase):
    """Class for testing the City class"""

    def setUp(self) -> None:
        """The setUp method"""
        self.cty = City()

    def tearDown(self) -> None:
        """The tearDown method"""
        self.cty = None

    def test_no_args_instantiation(self):
        """This class test the BaseModel Class"""

        self.assertIsInstance(self.cty, City)

    def test_attribute_type(self):
        """Test the atrribute of the User class"""

        self.assertTrue(isinstance(self.cty.state_id, str))
        self.assertTrue(isinstance(self.cty.name, str))

    def test_new_instance_stored_in_objects(self):
        """To test if the new instance of User are store in the file"""
        self.assertIn(self.cty, models.storage.all().values())
