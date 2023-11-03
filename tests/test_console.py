from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Test cases for this model"""
    def test_quit(self):
        """ Ensure that quit method is present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue().strip()
        self.assertEqual(output, "Quit command to exit the program")

    def test_EOF(self):
        """ Ensure that EOF is present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue().strip()
        self.assertEqual(output, "Quit command to exit the program")

    def test_empty_line(self):
        """ Ensure that line is empty"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_commands(self):
        """ Ensure that commands are present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        self.assertTrue(id)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel name "sam"')
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_all_method(self):
        """ Test 'all' method for all models"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            output = f.getvalue().strip()
        self.assertIsInstance(output, str)

    def test_count_method(self):
        """ Test 'count' method for models"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            output = f.getvalue().strip()
        try:
            output = int(output)
        except:
            pass
        self.assertTrue(isinstance(output, int))

    def test_show_method(self):
        """ Test 'show' method for models"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show('{}')".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)

    def test_destroy_method(self):
        """ Test 'destroy' method for models"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_update_method(self):
        """ Test 'update' method for models"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        self.assertTrue(id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.update("{}", name, "sam")'.format(id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
