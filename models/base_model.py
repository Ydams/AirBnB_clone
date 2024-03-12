#!/usr/bin/python
"""
"""

import uuid
from datetime import datetime
import models import get_storage

class BaseModel:
   def __init__(self, *args, **kwargs):
       """
       """

       if kwargs:
           for key,value in kwargs.items():
               if key in ["created_at", "updated_at"]:
                   value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
               setattr(self,key,value)
       else:
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()

   def save(self):
       self.updated_at = datetime.now()

   def to_dict(self):
       """
       """
       data = self.__dict__.copy()
       data['created_at'] = self.created_at.isoformat()
       data['updated_at'] = self.updated_at.isoformat()
       data['__class__'] = self.__class__.__name__

       return data

   def __str__(self):
       """
       """
       class_name = self.__class__.__name__
       return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

from models import storage
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    # Convert string to datetime
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self) # Add instance to filestorage

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['updated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        return new_dict

    def save(self):
        """
        storage = get_storage()
        
        """

# Test the BaseModel
if __name__ == "__main__":
    # Create an instance of BaseModel
    base_instance = BaseModel()

    # Convert instance to dictionary
    base_dict = base_instance.to_dict()

    # Recreate instance from dictionary
    recreated_instance = BaseModel(**base_dict)

    # Check if recreated instance matches original
    print("Original BaseModel ID:", base_instance.id)
    print("Recreated BaseModel ID:", recreated_instance.id)
    print("Original BaseModel created_at:", base_instance.created_at)
    print("Recreated BaseModel created_at:", recreated_instance.created_at)

