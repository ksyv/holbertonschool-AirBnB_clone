#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }
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

    def do_create(self, arg):
        'Creates a new instance of BaseModel and prints the id'
        if not arg:
            print("** class name missing **")
            return
        elif arg not in globals():
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        ' Prints the string representation of an instance'
        args = arg.split()
        dic_object = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in dic_object:
            print("** no instance found **")
        else:
            print(dic_object["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = arg.split()
        dict_object = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in dict_object.keys():
            print("** no instance found **")
        else:
            del dict_object["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances'
        dict_obj = storage.all()
        if arg:
            args = arg.split()
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            else:
                instances = [str(obj) for obj in dict_obj.values() if
                             type(obj).__name__ == args[0]]
        else:
            instances = [str(obj) for obj in dict_obj.values()]
        print(instances)

    def do_update(self, arg):
        'Updates an instance based on the class name and id'
        args = arg.split()
        dict_object = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in dict_object.keys():
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            key = f"{class_name}.{instance_id}"
            if key not in dict_object:
                print("** no instances found **")
            else:
                if attribute_name not in ['id', 'created_at', 'updated_at']:
                    if hasattr(dict_object[key], attribute_name):
                        existing_type = type(
                            getattr(dict_object[key], attribute_name))
                        if existing_type in [int, float, str]:
                            attribute_value = existing_type(attribute_value)
                setattr(dict_object[key], attribute_name, attribute_value)
                storage.save()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
