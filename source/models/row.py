import os, json, uuid
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
from models.index import Index
class Row:
    def __init__(self, table, value = None, primary_key = None):
        self.table = table
        if value is not None:
            self.__init_by_value(value)
        elif primary_key is not None:
            self.__init_by_primary_key()
        else:
            raise WrongInput(message = "the value and PK of the row is null")
        
    def __init_by_value(self, value):
        self.value = value
        self.primary_key = value[Keys.PRIMARY_KEY]

    def __init_by_primary_key(self,primary_key):
        self.primary_key = primary_key
        self.__get_by_primary_key()

    def serialize(self):
        self.__colomns_name_validate()
        if self.table.table_metadata.primary_key not in self.value : 
            self.value[self.table.table_metadata.primary_key] = str(uuid.uuid4().node)
        row_json_data = json.dumps(self.value, indent = 2)
        with open(self.get_path(), 'x') as row_file: 
            row_file.write(row_json_data)
        self.update_index()

    def row_exists(self):
        return os.path.isfile(self.get_path())

    def get_path(self):
        return os.path.join(self.table.get_path(), self.primary_key + ".json")

    def __colomns_name_validate(self):
        for row_colomn_name in self.value:
            if row_colomn_name not in self.table.table_metadata.columns:
                raise ColumnsNotExistInSchema(message = row_colomn_name + " is not exist in the schema of " + self.table.__table_name + " table")

    def update_index(self):
        for index_name in self.table.table_metadata.index_keys:
            index = Index(self, index_name = index_name, index_value = self.value[index_name])
            index.update_primary_key(primary_key = self.primary_key)
    
    def __get_by_primary_key(self):
        if not self.row_exists():
            return None
        with open(self.get_path(), 'r') as row_file:
            self.value = json.load(row_file)

    def delete(self):
        if self.row_exists():
            os.remove(self.get_path())
            for index_name in self.table.table_metadata.index_keys:
                index = Index(self, index_name = index_name, index_value = self.value[index_name])
                index.delete_primary_key(primary_key = self.primary_key, index_value = self.value[index_name])
        


