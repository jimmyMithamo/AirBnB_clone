#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    
    def postcmd(self, stop, line):
        # Check if the command matches the pattern <class name>.all()
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == 'all()':
            class_name = parts[0]
            if class_name in globals():
                self.do_all(class_name)
            
            
        return stop
    

    def do_quit(self, args):
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
                storage.save()
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

    def do_destroy(self, arg):
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
        obj_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))

        elif len(args) == 1:
            class_name = args[0]
            for key, obj in storage.all().items():
                    if class_name in key:
                        obj_list.append(str(obj))
            print(obj_list)            
            
                
                
            

        




    def do_update(self, arg):
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
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute_name = args[2]

        if len(args) == 3:
            print("** value missing **")
            return
        value = args[3]

        try:
            if key in storage.all():
                instance = storage.all()[key]

                if hasattr(instance, attribute_name):
                    # check attribute type in the storage
                    attr_type = type(getattr(instance, attribute_name))

                    # update the value
                    setattr(storage.all()[key], attribute_name, attr_type(value))
                    storage.save()
                else:
                    print("** attribute {} does not exist **".format(attribute_name))
            else:
                print("** key not found **")

        except Exception as e:
            print(" ** an error occured **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
