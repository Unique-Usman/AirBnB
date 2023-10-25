#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

"""The entry point of the whole 
program(a command interpreter)
"""


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the project
    """
    prompt = "(hbnb) "
    CLASSNAME = ["BaseModel", "User", "State", "City", "Place"]

    def do_EOF(self, line) -> bool:
        """Function to exit the interpreter gracefully"""
        return True

    def help_EOF(self) -> None:
        """Print the help text for EOF and quit"""
        print("Quit command to exit the program")

    def emptyline(self) -> None:
        """Overide the emptyline so that nothing happened
        when an empty line is typed
        """
        pass

    def precmd(self, line) -> str:
        """It remove trailing and leading space and \n from the argument"""
        return line.strip()

    def do_create(self, arg=None) -> None:
        """This command is for creating object

        The Object can be BaseModel, 

        Args:
            arg (str): The name of the object
        """
        if arg is None or not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            bm = BaseModel()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg) -> None:
        """This command is for showing instance

        The instance can be instance of any objects out of
        BaseModel, User, State, City, Place.

        To use the command :- 
        show <classname> <instance_id>
        """
        arg = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            bm = ".".join(arg)
            if bm not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[bm])

    def do_destroy(self, arg) -> None:
        """This command is for destroying instance

        The instance can be instance of any objects out of
        BaseModel, User, State, City, Place.

        To use the command :- 
        destroy <classname> <instance_id>
        """
        arg = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            bm = ".".join(arg)
            if bm not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[f"{bm}"]
                storage.save()

    def do_all(self, arg) -> None:
        """Return all the string representation of all instance base on the classname"""

        if arg not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            for key in all_objects:
                if arg in key:
                    print(all_objects[key])

    # assigning the value of EOF to quit.
    do_quit = do_EOF
    help_quit = help_EOF


if __name__ == "__main__":
    HBNBCommand().cmdloop()
