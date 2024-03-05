#!/usr/bin/python3
import cmd
"""Console Module"""


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

    # Basic command
    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        return True

    def emptyline(self):
        """
        Handles empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
