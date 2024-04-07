#!/usr/bin/python3
"""console module that represent the entry point to the app"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models import storage
from shlex import split as split
import models
import os
import cmd

app_classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "Amenity": Amenity, "Place": Place, "City": City,
               "Review": Review}


class HBNBCommand(cmd.Cmd):
    """class to handle the command line interpretr to act like the
    front-End for the AirBnB clone"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return (True)

    def do_EOF(self, line):
        """Exits the program"""
        return (True)

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates new instance and saves it to json file"""
        arg = line.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in app_classes:
            print("** class doesn't exist **")
        else:
            new_obj = app_classes[arg[0]]()
            print(new_obj.id)
            new_obj.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        arg = line.split()
        if not line:
            print("** class name missing **")
        elif arg[0] not in app_classes.keys():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            new_obj = "{}.{}".format(arg[0], arg[1])
            dic = models.storage.all()
            if new_obj not in dic:
                print("** no instance found **")
            else:
                print(dic[new_obj])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and save the changes to the json file"""
        arg = line.split()
        if not arg:
            print("** class name missing **")
            return False
        elif arg[0] not in app_classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            new_obj = "{}.{}".format(arg[0], arg[1])
            if new_obj not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_obj]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name."""
        arg = line.split()
        list_objs = []
        if not line:
            for new_obj in models.storage.all().values():
                list_objs.append(str(new_obj))
        else:
            if arg[0] in app_classes:
                for k, v in models.storage.all().items():
                    if v.__class__.__name__ == arg[0]:
                        list_objs.append(str(v))
            else:
                print("** class doesn't exist **")
                return False
        print(list_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        arg = line.split()

        if arg == "":
            print("** class name missing **")
        elif arg[0] not in app_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            new_obj = "{}.{}".format(arg[0], arg[1])
            if new_obj not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_obj], arg[2], arg[3])
                models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
