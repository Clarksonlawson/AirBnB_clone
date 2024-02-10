#!/usr/bin/python3

"""Console script for the AirBnB Clone Entry"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from helper import regParser

class HBNBCommand(cmd.Cmd):
    __OBJclasses = {
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

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argument = regParser(arg)
        
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
            storage.save()


    def do_show(self, arguments):
        """Show command Prints the string representation of an
        instance based on the class name and id
        """
        argument1 = regParser(arguments)
        objectDictionary = storage.all()

        if len(argument1) == 0:
            print("** class name missing **")
        elif argument1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument1[0], argument1[1]) not in objectDictionary:
            print("** no instance found **")
        else:
            print(objectDictionary["{}.{}".format(argument1[0], argument1[1])])

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""

        argument1 = regParser(argument)
        objectDictionary = storage.all()

        if len(argument1) == 0:
            print("** class name missing **")
        elif argument1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument1[0], argument1[1]) not in objectDictionary.keys():
            print("** no instance found **")
        else:
            del objectDictionary["{}.{}".format(argument1[0], argument1[1])]
            storage.save()


    def do_all(self, argument):
        """Prints all string representation of
        all instances based or not on the class name."""

        argument1 = regParser(argument)

        if len(argument1) > 0 and argument1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objects = []
            for obj in storage.all().values():
                if len(argument1) > 0 and argument1[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(argument1) == 0:
                    objects.append(obj.__str__())
            print(objects)

    def do_update(self, arguments):
        """Updates the instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)"""

        argument = regParser(arguments)
        objectDictionary = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        
        if argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        
        if "{}.{}".format(argument[0], argument[1]) not in objectDictionary.keys():
            print("** no instance found **")
            return False
        
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument) == 4:
            obj = objectDictionary["{}.{}".format(argument[0], argument[1])]
            
            if argument[2] in obj.__class__.__dict__.keys():
                valueType = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = valueType(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = objectDictionary["{}.{}".format(argument[0], argument[1])]

            for key, value in eval(argument[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valueType = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valueType(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


    def do_counter(self, arguments):
        """count <class> or <class>.count()
        Retrieve the number of instances of a given class."""

        argument = regParser(arguments)
        counter = 0
        for obj in storage.all().values():
            if argument[0] == obj.__class__.__name__:
                counter += 1
        print(counter)


    def default(self, arg):
        """Default behavior for cmd module 
        when input is invalid
        """
        argumentDictionary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        regMatch = re.search(r"\.", arg)
        
        if regMatch is not None:
            argument1 = [arg[:regMatch.span()[0]], arg[regMatch.span()[1]:]]
            regMatch = re.search(r"\((.*?)\)", argument1[1])

            if regMatch is not None:
                commandArr = [argument1[1][:regMatch.span()[0]], regMatch.group()[1:-1]]
                if commandArr[0] in argumentDictionary.keys():
                    call = "{} {}".format(argument1[0], commandArr[1])
                    return argumentDictionary[commandArr[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
