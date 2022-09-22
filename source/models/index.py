import os
from outputs.exceptions import *

class Index:
    def __init__(self, table, index_value):
        self.table = table
        self.index_value = index_value

    def serialize(self):
        os.makedirs(self.get_path(), exist_ok = True)
    
    def get_path(self):
        return os.path.join(self.table.get_path(), os.path.join("indices" , self.index_value))
    
    def add_primary_key(self, primary_key, index_value):
        index_value_file_path = os.path.join(self.get_path(), index_value + ".txt")
        old_primary_keys = set(self.get_primary_key(index_value))                
        old_primary_keys.add(primary_key)
        Index.__write_in_file(path = index_value_file_path, data = old_primary_keys)
    
    def delete_primary_key(self, primary_key, index_value):
        index_value_file_path = os.path.join(self.get_path(), index_value + ".txt")
        old_primary_keys = self.get_primary_key(index_value)
        old_primary_keys.remove(primary_key)
        Index.__write_in_file(path = index_value_file_path, data = old_primary_keys)

    def get_primary_key(self, index_value):
        index_value_file_path = os.path.join(self.get_path(), index_value + ".txt")
        if not os.path.isfile(index_value_file_path):
            return []
        with open(index_value_file_path, mode ="r") as index_file:
            primary_keys = index_file.read().split(",")
        return primary_keys
    
    def update_primary_key(self, primary_key, index_value):
        self.delete_primary_key(primary_key = primary_key, index_value = index_value)
        self.add_primary_key(primary_key = primary_key, index_value = index_value)

    @staticmethod
    def __write_in_file(path, data):
        with open(path, mode ="w") as index_file:
            index_file.write(",".join(data))