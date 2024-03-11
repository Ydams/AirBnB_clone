#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at()

    def save(self):
        """

        """
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
        class_name = self.__class__.name__
        return f'[{self.__class__.name__}] ({self.id}] {self.__dict__}'
