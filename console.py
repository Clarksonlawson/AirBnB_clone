#!/usr/bin/python3
"""Console script for the AirBnB Clone Entry"""
import cmd
from models.base_model import BaseModel
import re
from shlex import split
from models import storage
from helper import parse

class HBNBCommand(cmd.Cmd):
    """Console: the entry point class
    to the program"""

    _OBJCLasses = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"    
            }
     prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command that exits the program"""
        print("")
        return True
    def emptyline(self):
        """Empty line command that does no execution"""
        pass

    def do_create(self, obj):
        """Create command to create a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        _obj = parse(obj)
        if len(_obj) == 0:
            print("** class name missing **")
        elif _obj[0] not in HBNBCommand.__OBJclasses:
            print("** class doesn't exist **")
        else:
            print(eval(_obj[0])().id)
            storage.save()
    def do_show(self, obj):
        """Show command Prints the string representation of an
         instance based on the class name and id
         """
        _obj = parse(obj)
        _objDic = storage.all()

        if len(_objDic) == 0:
            print("** class name missing **")
        elif _obj[0] not in HBNBCommand.__OBJclasses:
            print("** class doesn't exist **")
        elif len(_obj) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(_obj[0], _obj[1]) not in _objDic.keys():
            print("** no instance found **")
        else:
            print(_objDic["{}.{}".format(_obj[0], _obj[1])])

    def do_destroy(self, obj):
        """Deletes an instance based on the class name and id """
        _obj = parse(obj)
        _objDic = storage.all()
        if len(_objDic) == 0:
            print("** class name missing **")
        elif _obj[0] not in HBNBCommand.__OBJclasses:
            print("** class doesn't exist **")
        elif len(_obj) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(_obj[0], _obj[1]) not in _objDic.keys():
            print("** no instance found **")
        else:
            del _objDic["{}.{}".format(_obj[0], _obj[1])]
            storage.save()

    def do_all(self, obj):
        """Prints all string representation of
        all instances based or not on the class name."""
        _obj = parse(obj)

        if len(_obj) > 0 and _obj[0] not in HBNBCommand.__OBJclasses:
            print("** class name missing **")
        else:
            _object = []
            for _objVal in storage.all().values():
                if len(_obj) > 0 and obj[0] == _objVal.__class__.__name__:
                    _object.append(_objVal.__str__())
                elif len(_obj) == 0:
                    _object.append(_objVal.__str__())
                else:
                    print(_object)
    def do_update(self, obj):
        """Updates the instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        arguments = parse(obj)
        objDic = storage.all()

        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in HBNBCommand.__OBJclasses:
            print("** class doesn't exist **")
            return False
        if len(arguments) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arguments[0], arguments[1]) in objDic.keys():
            print("** no instance found **")
            return False
        if len(arguments) == 2:
            print("** attribute name missing **")
            return False
        if len(arguments) == 3:
            try:
                type(eval(arguments[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arguments) == 4:
            newObj = objDic["{}.{}".format(arguments[0], arguments[1])]
            if arguments[2] in newObj.__class__.__dict__.keys():
                valueType = type(newObj.__class__.__dict__[arguments[2]])
                newObj.__dict__[arguments[2]] = valueType[arguments[3]]
            else:
                newObj.__dict__[arguments[2]] = arguments[3]
        else:
            newObj = objDic["{}.{}".format(arguments[0], arguments[1])]
            for key, value in eval(arguments[2]).items():
                if (key in newObj.__class__.__dict__.keys() and
                        type(newObj.__class__.__dict__[key]) in {str, int, float, bool}):
                    valueType = type(newObj.__class__.__dict__[key])
                    newObj.__dict__[key] = valueType[value]
                else:
                    newObj.__dict__[key] = value
        storage.save()

    def do_count(self, arguments):
        """count <class> or <class>.count()
        Retrieve the number of instances of a given class."""

        arguments = parse(arguments)
        counter = 0
        objectList = storage.all()

        for myObject in objectList.values():
            if arguments[0] == myObject.__class__.__name__:
                counter += 1
            print(counter)

    def default(self, line):
        print(f"Unknown command: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
