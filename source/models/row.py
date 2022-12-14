import os, json, uuid
from tracemalloc import Statistic
from outputs.exceptions import *
from models.index import Index

class Row:
    def __init__(self, table, value = {}):
        self.table = table
        Row.colomns_name_validate(table, value)
        self.__value = value
        if self.table.table_metadata.primary_key not in self.__value : 
            self.__value[self.table.table_metadata.primary_key] = str(uuid.uuid4().node)
    
    def get_primary_key(self):
        return self.__value[self.table.table_metadata.primary_key]
    
    @staticmethod
    def colomns_name_validate(table, query):
        for row_colomn_name in query:
            if row_colomn_name not in table.table_metadata.columns:
                raise ColumnsNotExistInSchema(message = row_colomn_name + " is not exist in the schema of " + table.get_name() + " table")
    
    def serialize(self):
        self.__lock()
        row_json_data = json.dumps(self.__value, indent = 2)
        with open(self.get_path(), 'w') as row_file: 
            row_file.write(row_json_data)
        for index_name in self.table.table_metadata.index_keys:
            if index_name not in self.get_value():continue
            index = self.table.table_metadata.indicies[index_name]
            index.add_primary_key(primary_key = self.get_primary_key(), index_value = self.__value[index_name])
        self.__unlock()

    def row_exists(self):
        return os.path.isfile(self.get_path())

    def get_path(self):
        return Row.get_row_path(self.table, self.get_primary_key()) 

    @staticmethod
    def get_row_path(table, primary_key):
        return os.path.join(table.get_Data_path(), primary_key + ".json")

    @staticmethod   
    def load_by_primary_key(table, primary_key):
        row_file_path = Row.get_row_path(table, primary_key)
        if not os.path.isfile(row_file_path) :
            return None
        with open(row_file_path, 'r') as row_file:
            value = json.load(row_file)
        return Row(table = table, value = value)

    def delete(self):
        self.__lock()
        if not self.row_exists():
            return
        os.remove(self.get_path())
        for index_name in self.table.table_metadata.index_keys:
            index = self.table.table_metadata.indicies[index_name]
            index.delete_primary_key(primary_key = self.get_primary_key(), index_value = self.__value[index_name])
 
        self.__unlock()

    def __lock(self):
        while True:
            try:
                with open(self.__get_lock_path(), "x"):
                    break
            except:
                pass

    def __unlock(self):
        os.remove(self.__get_lock_path())

    def __get_lock_path(self):
        return os.path.join(self.table.get_path(), os.path.join("Lock", self.get_primary_key() + ".json"))
    
    def has_attributes(self, query):
        row_value = self.get_value()
        for key in query:
            if row_value.get(key) is None or query[key] != row_value[key]:
                return False
        return True

    def get_value(self):
        return self.__value
    
    def get_all_primary_keys(table):
        primarykeys = os.listdir(table.get_Data_path())
        primarykeys_correct = []
        for primarykey in primarykeys :
            primarykeys_correct.append(primarykey.partition('.')[0])
        return primarykeys_correct
