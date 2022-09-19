import json, os
from commands_functions.schema_keys import Keys
from outputs.exceptions import *

class TableMetaData():
    def __init__(self, TB, table_shcema):
        self.TB_schema = table_shcema
        self.TB = TB
        self.name = table_shcema[Keys.NAME]
        self.columns = table_shcema[Keys.COLUMNS]
        self.PK = table_shcema[Keys.PK]
        self.index_keys = table_shcema[Keys.INDEX_KEY]
        self.consistently = table_shcema[Keys.CONSISTENTLY]

    def get_path(self):
        return self.TB.get_path()

    def serialize_table_shcema(self):
        TB_schemafile_path =  os.path.join(self.get_path(), self.TB.get_name() +".json" ) 
        with open(TB_schemafile_path, 'w') as table_schema_file:
            json.dump(self.TB_schema, table_schema_file,indent=2)
        self.serialize_indecies()

    def serialize_indecies(self):
        indeices_path = os.path.join(self.get_path(),"indices")
        os.makedirs(indeices_path, exist_ok = True)
        for index in self.index_keys: 
                os.makedirs(os.path.join(indeices_path,index), exist_ok = True)