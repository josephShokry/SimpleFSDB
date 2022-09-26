import json, os
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
from models.index import Index

class TableMetaData():
    def __init__(self, table, table_shcema):
        self.table_schema = table_shcema
        self.table = table
        self.name = table_shcema[Keys.NAME]
        self.columns = table_shcema[Keys.COLUMNS]
        self.primary_key = table_shcema[Keys.PRIMARY_KEY]
        self.index_keys = table_shcema[Keys.INDEX_KEY]
        self.consistently = table_shcema[Keys.CONSISTENTLY]
        self.enable_overwrite = table_shcema[Keys.ENABLE_OVERWRITE]

    def get_path(self):
        return self.table.get_path()

    def serialize_table_shcema(self):
        table_schemafile_path =  os.path.join(self.get_path(), "schema.json")
        with open(table_schemafile_path, 'w') as table_schema_file:
            json.dump(self.table_schema, table_schema_file,indent=2)
        self.serialize_indecies()

    def serialize_indecies(self):
        os.makedirs(os.path.join(self.get_path(),"indices"), exist_ok = True)
        for index_value in self.index_keys: 
            index = Index(table = self.table, index_value = index_value)
            index.serialize()