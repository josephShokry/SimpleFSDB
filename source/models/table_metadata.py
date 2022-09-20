import json, os
from commands_functions.schema_keys import Keys
from outputs.exceptions import *

class TableMetaData():
    def __init__(self, table, table_shcema):
        self.table_schema = table_shcema
        self.table = table
        self.name = table_shcema[Keys.NAME]
        self.columns = table_shcema[Keys.COLUMNS]
        self.primary_key = table_shcema[Keys.primary_key]
        self.index_keys = table_shcema[Keys.INDEX_KEY]
        self.consistently = table_shcema[Keys.CONSISTENTLY]

    def get_path(self):
        return self.table.get_path()

    def serialize_table_shcema(self):
        table_schemafile_path =  os.path.join(self.get_path(), self.table.get_name() +".json" ) 
        with open(table_schemafile_path, 'w') as table_schema_file:
            json.dump(self.table_schema, table_schema_file,indent=2)
        self.serialize_indecies()

    def serialize_indecies(self):
        indeices_path = os.path.join(self.get_path(),"indices")
        os.makedirs(indeices_path, exist_ok = True)
        for index in self.index_keys: 
                os.makedirs(os.path.join(indeices_path,index), exist_ok = True)