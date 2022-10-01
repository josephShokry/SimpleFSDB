import os

from commands_functions.schema_keys import Keys
from models.table import Table
from outputs.exceptions import *

class Database:
    def __init__(self, database_name = None, schema_data = None):
        self.tables = {}
        if schema_data is not None:
            self.__init_by_schema(schema_data = schema_data)
        elif database_name is not None:
            self.__init_by_name(database_name = database_name)
        else :
            raise WrongInput(message = "the database name or schema data are null")
            
    def __init_by_schema(self, schema_data):
        self.__database_name = schema_data[Keys.DATABASE_NAME]
        for table_schema in schema_data[Keys.TABLES]:
            self.tables[table_schema[Keys.NAME]] = Table(self, table_schema = table_schema)

    def __init_by_name(self, database_name):
        self.__database_name = database_name
        self.__database_name_validate()
        for table_name in os.listdir(self.get_path()):
            self.tables[table_name] = Table(self, table_name = table_name)
        

    def serialize(self):
        os.makedirs(self.get_path(), exist_ok = True)
        self.__serialize_tables()

    def __serialize_tables(self):
        #update tables_metadata dict
        for table in self.tables.values():
            table.serialize()

    def get_table(self,table_name):
        if table_name in self.tables.keys():
            return self.tables[table_name]
        raise TableNotExist(message = "the table name you entered is not valid or table is not exist")


    def set(self, table_name, row):
        table = self.get_table(table_name)
        table.set(row)
    
    def get(self, table_name, query):
        table = self.get_table(table_name)
        rows_obj = table.get(query)
        data = []
        for row in rows_obj:
            data.append(row.get_value())
        return data
    
    def delete(self, table_name, query):
        table = self.get_table(table_name)
        return table.delete(query) 
    
    def get_path(self):
        return os.path.join(os.getcwd(), self.__database_name)
    
    def get_name(self):
        return self.__database_name
   
    def __database_name_validate(self):
        if not os.path.isdir(self.get_path()):
            raise DatabaseNotExist(message = "the database name you entered is not valid or database is not exist")
