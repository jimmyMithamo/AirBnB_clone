#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


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
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
    def do_show(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id) 
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self,arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
        
    def do_all(self, arg):
        args = arg.split()

        obj_list =[]

        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] in globals():
            class_name = args[0]
            for key, obj in storage.all().items():
                if key.startswith(class_name + "."):
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print(obj_list)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
