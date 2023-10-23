#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

"""This module contains all the test to
test the BaseModel class
"""


class TestBaseModelInstantiation(unittest.TestCase):
    """This is the class for testing the BaseModel class"""

    def setUp(self) -> None:
        """To prepare the necessary requirement/environment/variable
        to run the test
        """

        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self) -> None:
        """The tearDown class"""

        self.bm1 = None
        self.bm2 = None

    def test_no_args_instantiation(self):
        """This class test the BaseModel Class"""

        self.assertIsInstance(self.bm1, BaseModel)
    
    def test_instance_id(self):
        """Test the id attribute of the BaseModel class
        
        Test if the attribute is present
        Test if the type of the attribute is a str type
        """
        self.assertTrue(hasattr(self.bm1, "id"))
        if hasattr(self.bm1, "id"):
            self.assertTrue(isinstance(self.bm1.id, str))

    def test_instance_created_at(self):
        """Test the created_at attribute of the BaseModel class

        Test if the attribute is present
        Test if the attribute is a datetime type
        """
        self.assertTrue(hasattr(self.bm1, "created_at"))
        if hasattr(self.bm1, "created_at"):
            self.assertTrue(isinstance(self.bm1.created_at, datetime))

    def test_instance_updated_at(self):
        """Test the updated_at attribute of the BaseModel class

        Test if the attribute is present
        Test if the attribute is a datetime type
        """
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        if hasattr(self.bm1, "updated_at"):
            self.assertTrue(isinstance(self.bm1.updated_at, datetime))

    def test_two_models_unique_ids(self):
        """Test if two instance of BaseModel does not have the same unique id"""
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_two_models_different_created_at(self):
        """Test the created_at of two instance of the BaseModel
            
        They must not be equal
        """
        self.assertLess(self.bm1.created_at, self.bm2.created_at)

    def test_two_models_different_updated_at(self):
        """Test the updated_at of two instance of the BaseModel
            
        They must not be equal
        """
        self.assertLess(self.bm1.updated_at, self.bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModelSaveToFile(unittest.TestCase):
    """ Class for testing the save() method in the BaseModel class"""
    def setUp(self) -> None:
        """To prepare the necessary requirement/environment/variable
        to run the test
        """
        try:
            os.rename("file.json", "tmp")
        except OSError:
            pass

        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
 
    def tearDown(self) -> None:
        """To clean the variable, environment, requirement after test"""
        try:
            os.remove("file.json")
        except OSError:
            pass
        try:
            os.rename("tmp", "file.json")
        except OSError:
            pass

        self.bm1 = None
        self.bm2 = None

    def test_one_save(self):
        first_updated_at = self.bm1.updated_at
        self.bm1.save()
        self.assertLess(first_updated_at, self.bm1.updated_at)

    def test_two_saves(self):
        first_updated_at = self.bm1.updated_at
        self.bm1.save()
        second_updated_at = self.bm2.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        self.bm1.save()
        self.assertLess(second_updated_at, self.bm1.updated_at)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.bm1.save(None)

    def test_save_updates_file(self):
        self.bm1.save()
        bmid = "BaseModel." + self.bm1.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def setUp(self):
        """To prepare the necessary requirement/environment/variable
        to run the test
        """
        self.bm = BaseModel()

    def test_to_dict_type(self):
        self.assertTrue(dict, type(self.bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        self.assertIn("id", self.bm.to_dict())
        self.assertIn("created_at", self.bm.to_dict())
        self.assertIn("updated_at", self.bm.to_dict())
        self.assertIn("__class__", self.bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        self.bm.name = "Holberton"
        self.bm.my_number = 98
        self.assertIn("name", self.bm.to_dict())
        self.assertIn("my_number", self.bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm_dict = self.bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        self.bm.id = "123456"
        self.bm.created_at = self.bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(self.bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        self.assertNotEqual(self.bm.to_dict(), self.bm.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.bm.to_dict(None)

if __name__ == "__main__":
    unittest.main()
