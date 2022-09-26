import os, json, uuid
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
from models.index import Index

class Row:
    def __init__(self, table, value = None):
        self.table = table
        self.value = value
        if self.table.table_metadata.primary_key not in value : 
            value[self.table.table_metadata.primary_key] = str(uuid.uuid4().node)
        self.primary_key = value[self.table.table_metadata.primary_key]

    def serialize(self):
        self.__lock()
        self.__colomns_name_validate()
        if self.table.table_metadata.primary_key not in self.value : 
            self.value[self.table.table_metadata.primary_key] = str(uuid.uuid4().node)
        row_json_data = json.dumps(self.value, indent = 2)
        with open(self.get_path(), 'w') as row_file: 
            row_file.write(row_json_data)
        self.update_index()
        self.__unlock()

    def row_exists(self):
        return os.path.isfile(self.get_path())

    def get_path(self):
        return os.path.join(self.table.get_path(),os.path.join("Data", self.primary_key + ".json"))

    def __colomns_name_validate(self):
        for row_colomn_name in self.value:
            if row_colomn_name not in self.table.table_metadata.columns:
                raise ColumnsNotExistInSchema(message = row_colomn_name + " is not exist in the schema of " + self.table.__table_name + " table")

    def update_index(self):
        for index_name in self.table.table_metadata.index_keys:
            index = Index(self.table, index_name = index_name, index_value = self.value[index_name])
            index.update_primary_key(primary_key = self.primary_key) ##update
    
    @staticmethod
    def load_by_primary_key(table, primary_key):
        row_file_path = os.path.join(table.get_path(), primary_key + ".json")
        if not os.path.isfile(row_file_path) :
            return None
        with open(row_file_path, 'r') as row_file:
            value = json.load(row_file)
        return Row(value = value)

    def delete(self):
        self.__lock()
        if not self.row_exists():
            return
        os.remove(self.get_path())
        for index_name in self.table.table_metadata.index_keys:
            index = Index(self, index_name = index_name, index_value = self.value[index_name])
            index.delete_primary_key(primary_key = self.primary_key, index_value = self.value[index_name])
        self.__unlock()

    def __lock(self):
        lock_file_path = os.path.join(self.table.get_path(), os.path.join("Lock", self.primary_key + ".json"))
        try:
            with open(lock_file_path, "x")as lock_file:
                pass
        except:
            raise FileNotFound(message = "the primary key is locked now try again later")

    def __unlock(self):
        lock_file_path = os.path.join(self.table.get_path(), os.path.join("Lock",self.primary_key + ".json"))
        os.remove(lock_file_path)
        pass