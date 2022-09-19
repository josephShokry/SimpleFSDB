import os, json

from commands_functions.schema_keys import Keys
from models.table import Table
from outputs.exceptions import *

class Database:
    def __init__(self, DB_name = None, schema_path = None):
        if schema_path is not None:
            self.schema_data = self.validate_schema_path(schema_path)
        else:
            self.tables = {}
            for table_schema in self.schema_data[Keys.TABLES]:
                self.tables[table_schema[Keys.NAME]] = Table(self, table_schema)

        self.DB_name = self.schema_data[Keys.DB_NAME]
        self.path = os.path.join(os.getcwd(), self.DB_name)

    @staticmethod
    def validate_schema_path(schema_path):
        if not os.path.exists(schema_path) :
            raise FileNotFound(status = Status.FileNotFound, message = "the schema path is not valid")
        with open(schema_path, 'r') as schema_file: 
            try:
                schema_data = json.load(schema_file)
            except:
                raise WrongInput(status = Status.WrongInput, message = "schema is written in a wrong json format")
        return schema_data

    def serialize(self):
        os.makedirs(self.path, exist_ok = True)
        self.__serialize_tables()

    def __serialize_tables(self):
        #update tables_metadata dict
        for table_schema in self.schema_data[Keys.TABLES]:
            table = Table(DB = self, table_schema = table_schema)
            table.serialize()

    def set(self, table_name, row):
        # table = Table(table_name)
        # table.set(row)
        pass
    
    def get(self, table, quiry):
        pass
    
    def delete(self, table, quiry):
        pass
    
    def get_path(self):
        return os.path.join(os.getcwd(), self.DB_name)
    
    def get_name(self):
        return self.DB_name