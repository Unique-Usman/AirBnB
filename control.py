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
    CLASSNAME = ["BaseModel", "User"]
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

    def do_create(self, arg=None) -> None:
        """This command is for creating object

        The Object can be BaseModel, 

        Args:
            arg (str): The name of the object
        """
        if arg is None or not arg.strip():
            print("** class name missing **")
        elif arg == "BaseModel":
            bm = BaseModel()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        arg = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.CLASSNAME:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            bm = ".".join(arg)
            if bm not in all_objects:
                #print(bm)
                print("** no instance found **")
            else:
                #clss = eval(arg[0])
                print(all_objects[bm])

    # assigning the value of EOF to quit.
    do_quit = do_EOF
    help_quit = help_EOF

if __name__ == "__main__":
    HBNBCommand().cmdloop()
