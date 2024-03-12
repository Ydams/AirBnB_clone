#!/usr/bin/python3
"""This file execute what the command interpreter gives it"""


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Handles empty line + ENTER"""
        pass

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

