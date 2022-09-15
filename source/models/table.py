from abc import ABC
import json, os
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
        return self.schema_data["name"]

    def getColumns(self):
        return self.schema_data["columns"]

    def getIndices(self):
        return self.schema_data["indices"]
        
    def getPrimaryKey(self):
        return self.schema_data["primary_key"]

class Table(TableMetaData):
    def __init__(self,DB_name, TB_name):
        self.loadTableSchema(DB_name, TB_name)

    def validate_overwrite(self,disable_overwrite,row_obj):
        #print("#################333")
        #print(disable_overwrite)
        #print(os.getcwd())
        #print(os.path.isfile(self.table_path + "\\" + self.getPrimaryKey() + ".json"))
        #print(os.path.isdir(self.table_path + "\\" + self.getPrimaryKey() ))
        if disable_overwrite and os.path.isfile(self.table_path + "\\" + row_obj[self.getPrimaryKey()] + ".json"):
            raise RowExists
        
    def writeNewRow(self,row_obj, disable_overwrite):
        self.validate_overwrite(disable_overwrite,row_obj)
        json_data = json.dumps(row_obj, indent = 2)
        with open(self.table_path + "\\" + row_obj[self.getPrimaryKey()] + ".json", 'w') as row_file: 
            row_file.write(json_data)
    
    def load_value(self, value = None, value_path = None):
        if value == None and value_path == None :
            raise WrongInput(message = "missing some inputs")

        if value_path is not None: # if he entered the path of the value which will be set
            if not os.path.isfile(value_path):
                raise FileNotFound(message = "the value file is not found")
            else:
                with open(value_path,"r")as value_file:
                    try:
                        json_obj = json.load(value_file)
                    except: raise WrongInput(message = "the json in the value path is not valid")
        elif value is None:
            raise WrongInput(message = "the value and the value path are both missed")
        
        else:
            try:
                json_obj = json.loads(value)
            except: raise WrongInput(message = "the value json in not valid")

        if self.getPrimaryKey() not in json_obj:
            raise WrongInput(message = "The value json text is invalid, it has not any id parameter")
        
        for column in json_obj:
            if column not in self.getColumns():
                raise ColumnsNotExistInSchema(message = column + " coloumn is not exist in the table schema")
        return json_obj
        