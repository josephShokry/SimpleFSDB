from dataclasses import dataclass
import json, os
from commands_functions.schema_keys import Keys
from models.table_metadata import TableMetaData
from outputs.exceptions import *
from models.index import Index


class Table:
    def __init__(self, database , table_name = None, table_schema = None):  
        self.database = database
        if table_schema is not None:
            self.__init_by_schema(table_schema = table_schema)
        elif table_name is not None:
            table_schema = self.__init_by_name(table_name = table_name)
        else :
            raise WrongInput(message = "the table name and table schema data are null")
        self.table_metadata = TableMetaData(self, table_schema)

    def __init_by_schema(self, table_schema):
        self.__table_name = table_schema[Keys.NAME]

    def __init_by_name(self, table_name):
        self.__table_name = table_name
        with open(os.path.join(self.get_path(), "schema.json"),"r")as table_schema_file:
            table_schema = json.load(table_schema_file)
        return table_schema

    def serialize(self):
        os.makedirs(self.get_path(),exist_ok = True)
        self.table_metadata.serialize_table_shcema()

    def get_path(self):
        return os.path.join(self.database.get_path(), self.get_name())
        
    def get_name(self):
        return self.__table_name

    def set(self, row):
        row_json_data = json.dumps(row, indent = 2)
        with open(os.path.join(self.get_path(), str(row[self.table_metadata.primary_key]) + ".json"), 'w') as row_file: 
            row_file.write(row_json_data)
        self.update_indx(row)

    
    def get(self):
        pass
    
    def delete(self):
        pass

    def update_indx(self, row):
        primary_key = row[self.table_metadata.primary_key]
        for index_name in self.table_metadata.index_keys:
            index = Index(self, index_name = index_name, index_value = row[index_name])
            index.add_primary_key(primary_key = primary_key)