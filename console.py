#!/usr/bin/python3
'''
Module: console.py
'''

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''defines the entry point of the command interpreter'''
    prompt = "(hbnb)"
    model_classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        ''' close program and save program
        using CTRL + D
        '''
        print("")
        return True

    def do_help(self, arg):
        '''help center command '''
        return super().do_help(arg)

    def emptyline(self):
        """defines an empty function"""
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        '''
        tokens = arg.split()
        if not validator(tokens, check_id=False):
            return
        obj = HBNBCommand.model_classes[tokens[0]]()
        obj.save()
        print(obj.id)

    def validator(tokens, check_id=False):
        '''validate class entry'''
        if not tokens:
            print("* class name missing **")
            return False
        if tokens[0] not in HBNBCommand.model_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(tokens) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def do_show(self, arg):
        '''
        Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        '''
        tokens = arg.split()
        if not validator(tokens, check_id=True):
            return
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(tokens[0], tokens[1])
        obj_instance = objs.get(key, None)
        if obj_instance is None:
            print("** no instance found **")
            return
        print(obj_instance)

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        '''
        tokens = arg.split()
        if not validator(tokens, check_id=True):
            return
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(tokens[0], tokens[1])
        obj_instance = objs.get(key, None)
        if obj_instance is None:
            print("** no instance found **")
            return
        del obj_instance[key]
        storage.save()

    def do_all(self, arg):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        '''
        tokens = arg.split()
        storage.reload()
        objs = storage.all()
        if len(tokens) < 1:
            print(["{}".format(str(v)) for _, v in objs.items()])
            return
        if tokens[0] not in HBNBCommand.model_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in objs.items() if type(v).__name__ == tokens[0]])
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
