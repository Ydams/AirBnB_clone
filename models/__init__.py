#!/usr/bin/python3

from models.engine.file_storage import FileStorage

def get_storage():
    global storage
    if 'storage' not in globals():
        storage = FileStorage()
    return storage

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

