#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
    def get_base_model():
        from models.base_model import BaseModel
        return BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        base_model = get_base_model()
        """
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create objects based on class name
                    class_obj = globals()[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    from models import storage

    # Reload objects from storage
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    # Create a new object
    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

