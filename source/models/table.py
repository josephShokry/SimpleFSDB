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
    
    def set(self, data):
        row_obj = Row(table = self, value = data)
        if row_obj.row_exists() and self.table_metadata.enable_overwrite == "false":
            raise RowExists(message = "this row is already exists and can't overwrite")
        elif row_obj.row_exists():
            old_row = Row.load_by_primary_key(table = self, primary_key = row_obj.get_primary_key())
            old_row.delete()
        row_obj.serialize()

    def get_similar_primarykeys(self, query):
        primarykeys = []
        for index_name in query:
            if index_name in self.table_metadata.index_keys:
                primarykeys = self.table_metadata.indicies[index_name].get_primary_key(index_value = query[index_name])
                if not len(primarykeys):
                    return None
                break
        return primarykeys
 
    def get(self, query):
        Row.colomns_name_validate(self, query)
        primarykeys = []
        if self.table_metadata.primary_key in query : # if primarykey in the query
            primarykeys.append(query[self.table_metadata.primary_key])     
        else:
            primarykeys = self.get_similar_primarykeys(query = query)
            if primarykeys is None:
                return []
            elif len(primarykeys) == 0:
                primarykeys = Row.get_all_primary_keys(self)# compare all data in the table with the query
        row_objects = self.get_rows(primarykeys)
        return Table.filter_by_query(row_objects = row_objects, query = query)

    def get_rows(self, primarykeys):
            row_objects = []
            for primarykey in primarykeys:
               row = Row.load_by_primary_key(self, primarykey)
               if row is not None: row_objects.append(row)
            return row_objects
            
    @staticmethod
    def filter_by_query(row_objects, query):
        filtered_objects = []
        for row_object in row_objects:
            if row_object.has_attributes(query = query):
                filtered_objects.append(row_object)
        return filtered_objects

    def delete(self, query):
        rows_obj = self.get(query)
        for row in rows_obj:
            row.delete()
    
    def __table_name_validate(self):
        if not os.path.isdir(self.get_path()):
            raise TableNotExist(message = "the database name you entered is not valid or database is not exist")

    def get_Data_path(self):
        return os.path.join(self.get_path(), "Data")
