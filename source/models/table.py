from abc import ABC
from dataclasses import dataclass
import json, os
from commands_functions.schema_keys import Keys
from models.table_metadata import TableMetaData
from outputs.exceptions import *


class Table:
    def __init__(self, database , table_name = None, table_schema = None):
        self.database = database
        if table_schema is not None:
            self.__table_name = table_schema[Keys.NAME]
        else :
            self.__table_name = table_name
            with open(self.get_path(),"r")as table_schema_file:
                table_schema = json.load(table_schema_file)

        self.table_metadata = TableMetaData(self, table_schema)

    def serialize(self):

        os.makedirs(self.get_path(),exist_ok = True)
        self.table_metadata.serialize_table_shcema()

    def get_path(self):
        return os.path.join(self.database.get_path(), self.get_name())
        
    def get_name(self):
        return self.__table_name

    def set(self):
        pass
    
    def get(self):
        pass
    
    def delete(self):
        pass