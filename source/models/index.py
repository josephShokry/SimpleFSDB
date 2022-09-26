import os
from outputs.exceptions import *

class Index:
    def __init__(self, table, index_value):
        self.table = table
        self.index_value = index_value

    def serialize(self):
        os.makedirs(self.get_path(), exist_ok = True)
    
    def get_path(self, index_value = None):
        if index_value == None:
            return os.path.join(self.table.get_path(), os.path.join("indices" , self.index_value))
        else:
            return os.path.join(self.get_path(), self.index_value + ".txt")

    def add_primary_key(self, primary_key, index_value):
        old_primary_keys = set(self.get_primary_key(index_value))                
        old_primary_keys.add(primary_key)
        Index.__write_in_file(path = self.get_path(index_value), data = old_primary_keys)
    
    def delete_primary_key(self, primary_key, index_value):
        old_primary_keys = self.get_primary_key(index_value)
        old_primary_keys.remove(primary_key)
        Index.__write_in_file(path = self.get_path(index_value), data = old_primary_keys)

    def get_primary_key(self, index_value):
        if not os.path.isfile(self.get_path(index_value)):
            return []
        with open(self.get_path(index_value), mode ="r") as index_file:
            primary_keys = index_file.read().split(",")
        return primary_keys
    
    def update_primary_key(self, primary_key):
        self.delete_primary_key(primary_key = primary_key, index_value = self.index_value)
        self.add_primary_key(primary_key = primary_key, index_value = self.index_value)

    def __write_in_file(self, data):
        with open(self.get_index_value_path(self.index_value), mode ="w") as index_file:
            index_file.write(",".join(data))