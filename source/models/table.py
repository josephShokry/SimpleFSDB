from dataclasses import dataclass
import json, os
from commands_functions.schema_keys import Keys
from models.index import Index
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

 
    def __table_name_validate(self):
            if not os.path.isdir(self.get_path()):
                raise TableNotExist(message = "the table name you entered is not valid or table is not exist")
    
    def set(self, row):
        self.__colomns_name_validate(row = row)
        row_obj = Row(table = self, value = row)
        if row_obj.row_exists() and self.table_metadata.enable_overwrite == "false":
            raise RowExists(message = "this row is already exists and can't overwrite")
        elif row_obj.row_exists():
            old_row = Row(table = self).load_by_primary_key(table=self, primary_key = row_obj.primary_key)
            old_row.delete()
        row_obj.serialize()


    def get_similar_primarykeys(self, query):
        primarykeys = []
        for index_name in query:
            if index_name in self.table_metadata.index_keys:
                primarykeys = Index(self, index_name = index_name, index_value = query[index_name]).get_primary_key(index_value = query[index_name])
                break
        return primarykeys
 

    def get(self, query):
        self.__colomns_name_validate(query)
        primarykeys = []
        if Keys.PRIMARY_KEY in query : # if primarykey in the query
            primarykeys.append(query[Keys.PRIMARY_KEY])     
        else:
            primarykeys = self.get_similar_primarykeys(query = query)
            if not len(primarykeys):# compare all data in the table with the query
                primarykeys = self.get_all_primary_keys()
        row_objects = self.get_rows(primarykeys)
        return self.filter_by_query(row_objects = row_objects, query = query)


    def get_rows(self, primarykeys):
            row_objects = []
            for primarykey in primarykeys:
               row_objects.append(Row(self).load_by_primary_key(self, primarykey))
            return row_objects


    def filter_by_query(self, row_objects, query):
        filtered_objects = []
        for row_object in row_objects:
            if Table.compare(query = query, row_object = row_object):
                filtered_objects.append(row_object.value)
        return filtered_objects


    @staticmethod
    def compare(query, row_object):
        row_value = row_object.value
        for key in query:
            if query[key] != row_value[key]:
                return False
        return True

    def delete(self):
        pass
    

    #to check that all the givin colomns in the value are in the table schema
    def __colomns_name_validate(self, row):
        for row_colomn_name in row:
            if row_colomn_name not in self.table_metadata.columns:
                raise ColumnsNotExistInSchema(message = row_colomn_name + " is not exist in the schema of " + self.__table_name + " table")
    
    def get_all_primary_keys(self):
        primarykeys = os.listdir(os.path.join(self.get_path(), "Data"))
        primarykeys_correct = []
        for primarykey in primarykeys :
            primarykeys_correct.append(primarykey.partition('.')[0])
        return primarykeys_correct 
