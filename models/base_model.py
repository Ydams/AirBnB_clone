#!/usr/bin/python
"""
"""

import uuid
from datetime import datetime
import models

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



import uuid
from datetime import datetime

class User(BaseModel):
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

my_model_json = {
    'id': '123',
    'created_at': '2022-01-01T00:00:00.000',
    'updated_at': '2022-01-01T00:00:00.000',
    'name': 'John Doe',
    'age': 30
}

my_new_model = User(**my_model_json)
print(my_new_model)
