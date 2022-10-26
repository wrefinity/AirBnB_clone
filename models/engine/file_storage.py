#!/usr/bin/python3
'''
Module: FileStorage
'''
import os
import json


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
        key = "{}.{}".format(type(self).__name__, self.id)
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        with open(FileStorage.__path, 'w') as file:
            dc = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dc, file)
