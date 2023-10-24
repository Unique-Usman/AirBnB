#!/usr/bin/python3
import cmd

"""The entry point of the whole 
program(a command interpreter)
"""


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the project
    """
    prompt = "(hbnb) "

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

    # assigning the value of EOF to quit.
    do_quit = do_EOF
    help_quit = help_EOF

if __name__ == "__main__":
    HBNBCommand().cmdloop()
