from abc import ABC
from dataclasses import dataclass
import json, os
from commands_functions.schema_keys import Keys
from models.table_metadata import TableMetaData
from outputs.exceptions import *


class Table:
    def __init__(self, DB , table_name = None, table_schema = None):
        if table_schema is not None:
            self.__TB_name = table_schema[Keys.NAME]
        else :
            self.__TB_name = table_name
        self.DB = DB
        self.TB_schema_data = table_schema
        self.TB_metadata = TableMetaData(self, table_schema)

    def serialize(self):

        os.makedirs(self.get_path(),exist_ok = True)
        self.TB_metadata.serialize_table_shcema()

    def get_path(self):
        return os.path.join(self.DB.get_path(), self.get_name())
        
    def get_name(self):
        return self.__TB_name

    def set(self):
        pass
    
    def get(self):
        pass
    
    def delete(self):
        pass