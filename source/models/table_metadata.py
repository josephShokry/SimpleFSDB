from abc import ABC
import json, os
from commands_functions.schema_keys import Keys
from outputs.exceptions import *

class TableMetaData(ABC):
    def loadTableSchema(self, DB_name, table_name):
        #validate that 2 para is not null
        self.validate_DB_TB(DB_name, table_name)
        self.DB_name = DB_name
        self.table_name = table_name
        self.table_path = str(DB_name) + "\\" + str(table_name)
        table_schema_path = self.table_path + "\\schema.json"
        with open(table_schema_path,"r")as schema_file:
            self.schema_data = json.load(schema_file)
    
    def validate_DB_TB(self, DB_name, TB_name):
        if DB_name == None or TB_name == None :
            raise WrongInput(message = "missing some inputs")
        if not os.path.isdir(DB_name):
            raise DatabaseNotExist()

        if not os.path.exists(DB_name + "\\" + TB_name):
            raise TableNotExist()
    
    def getTableName(self):
        return self.schema_data[Keys.NAME]

    def getColumns(self):
        return self.schema_data[Keys.COLUMNS]

    def getIndices(self):
        return self.schema_data[Keys.INDEX_KEY]
        
    def getPrimaryKey(self):
        return self.schema_data[Keys.PK]
