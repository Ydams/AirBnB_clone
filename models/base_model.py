#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base class for all models.
    """

    def __init__(self, **kwargs):
        """
        Initialize the instance.

        :param kwargs: Arbitrary keyword arguments.
        """
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

        for key, value in kwargs.items():
            if key not in ['id', 'created_at', 'updated_at']:
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def save(self):
        """
        Save the instance.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        data['__class__'] = self.__class__.__name__

        return data

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'
