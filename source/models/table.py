from dataclasses import dataclass
import json, os
from commands_functions.schema_keys import Keys
from models.row import Row
from models.table_metadata import TableMetaData
from outputs.exceptions import *


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
        self.__table_name_validate()
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
        self.__colomns_name_validate(row = row)
        row_obj = Row(table = self, value = row)
        print("###########new data########################")
        print(row_obj.value)
        print("##############################################")
        if row_obj.row_exists() and self.table_metadata.enable_overwrite == "false":
            raise RowExists(message = "this row is already exists and can't overwrite")
        elif row_obj.row_exists():
            old_row = Row(table = self).load_by_primary_key(table=self, primary_key = row_obj.primary_key)
            print("###########old data########################")
            print(old_row.value)
            print("##############################################")
            old_row.delete()
        row_obj.serialize()

    
    def get(self):
        pass
    
    def delete(self):
        pass

    # def update_indx(self, row):
    #     primary_key = row[self.table_metadata.primary_key]
    #     for index_name in self.table_metadata.index_keys:
    #         index = Index(self, index_name = index_name, index_value = row[index_name])
    #         index.add_primary_key(primary_key = primary_key)
    
    def __table_name_validate(self):
        if not os.path.isdir(self.get_path()):
            raise TableNotExist(message = "the database name you entered is not valid or database is not exist")

    #to check that all the givin colomns in the value are in the table schema
    def __colomns_name_validate(self, row):
        for row_colomn_name in row:
            if row_colomn_name not in self.table_metadata.columns:
                raise ColumnsNotExistInSchema(message = row_colomn_name + " is not exist in the schema of " + self.__table_name + " table")
    
    def get_primary_keys(self):
        return os.listdir(self.get_path())
