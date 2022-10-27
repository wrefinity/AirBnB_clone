#!/usr/bin/python3
'''
Module: FileStorage
'''
from os.path import exists
import json
from models.base_model import BaseModel


class FileStorage():
    '''
    the class FileStorage, serializes instances to a JSON file
    and deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        with open(FileStorage.__file_path, 'w') as file:
            dc = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dc, file)

    def reload(self):
        '''
        Deserialize the json file
        '''
        if not exists(FileStorage.__file_path):
            return
        model_classes = {'BaseModel': BaseModel}

        with open(FileStorage.__file_path, 'r') as file:
            de_serialize = None
            try:
                de_serialize = json.load(file)
                if de_serialize is None:
                    return
            except json.JSONDecodeError:
                pass
            FileStorage__objects = {
                    key: model_classes[key.split('.')[0]](**val)
                    for key, val in de_serialize.items()}
