#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_quit(self,args):
        """Quit command to exit the programe
        """
        return True

    def do_EOF(self, args):
        """command to quit the program"""
        return True
    def emptyline(self):
        """does nothing when an empty line is entered"""
        pass





if __name__ == '__main__':
    HBNBCommand().cmdloop()
