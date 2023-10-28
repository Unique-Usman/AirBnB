#!/usr/bin/python3
from models.user import User
import unittest
import models

"""Module for testing the User module(User class)"""

class TestUserClass(unittest.TestCase):
    """Class for testing the User class"""

    def setUp(self) -> None:
        """The setUp method"""
        self.usr = User()

    def tearDown(self) -> None:
        """The tearDown method"""
        self.usr = None

    def test_no_args_instantiation(self):
        """This class test the BaseModel Class"""

        self.assertIsInstance(self.usr, User)

    def test_attribute_type(self):
        """Test the atrribute of the User class"""

        self.assertTrue(isinstance(self.usr.email, str))
        self.assertTrue(isinstance(self.usr.password, str))
        self.assertTrue(isinstance(self.usr.first_name, str))
        self.assertTrue(isinstance(self.usr.last_name, str))

    def test_new_instance_stored_in_objects(self):
        """To test if the new instance of User are store in the file"""
        self.assertIn(self.usr, models.storage.all().values())

    def test_save_update_user(self):
        """To test that the user can be updated and save"""
        
        self.usr.first_name = "Betty"
        self.usr.last_name = "Bar"
        self.usr.email = "airbnb@mail.com"
        self.usr.password = "root"
        self.assertTrue(self.usr.first_name, "Betty")
        self.assertTrue(self.usr.last_name, "Bar")
        self.assertTrue(self.usr.email, "airbnb@mail.com")
        self.assertTrue(self.usr.password, "root")
