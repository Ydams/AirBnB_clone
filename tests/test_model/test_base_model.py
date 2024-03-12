#!/usr/bin/python3
"""

"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_instance = BaseModel()

    def tearDown(self):
        del self.base_instance

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.base_instance, 'id'))
        self.assertTrue(hasattr(self.base_instance, 'created_at'))
        self.assertTrue(hasattr(self.base_instance, 'updated_at'))

    def test_id_type(self):
        self.assertIsInstance(self.base_instance.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_instance.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_instance.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_instance.updated_at
        self.base_instance.save()
        new_updated_at = self.base_instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_instance = BaseModel()
        self.test_json_file = "test_file.json"

    def tearDown(self):
        del self.storage
        del self.base_instance
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)

    def test_new_method(self):
        self.assertIn("BaseModel." + self.base_instance.id, self.storage.all())

    def test_save_method(self):
        self.base_instance.save()
        with open(self.test_json_file, 'r') as file:
            data = file.read()
            self.assertTrue(data)
            self.assertIn("BaseModel." + self.base_instance.id, data)

    def test_reload_method(self):
        self.base_instance.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.base_instance.id, self.storage.all())

    def test_all_method(self):
        self.base_instance.save()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel." + self.base_instance.id, all_objs)


if __name__ == '__main__':
    unittest.main()

