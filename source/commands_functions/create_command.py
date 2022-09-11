import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
from outputs.status import Status

class CreateCommand(AbtractCommand):
    def __init__(self, schema_path):
        self.schema_data = CreateCommand.__validate(schema_path)

    @staticmethod  
    def __validate(schema_path):
        if schema_path == None or not os.path.exists(schema_path) :
            raise MissingInput(status = Status.MissingInput, message = "the schema is missing")
        with open(schema_path, 'r') as schema: 
            try:
                schema_data = json.load(schema)
            except:
                raise WrongInput(status = Status.WrongInput, message = "schema is written in a wrong json format")
        return schema_data

    def execute(self):
        parent_dir = os.getcwd() #get the current dir of the project
        data_base_name = self.schema_data[Keys.DB_NAME]
        path = os.path.join(parent_dir, data_base_name)
        os.makedirs(path, exist_ok = True)
        if not Keys.TABLES in self.schema_data:
            return
        for table in self.schema_data[Keys.TABLES]:
            table_path = os.path.join(path, table[Keys.NAME])
            os.makedirs(table_path, exist_ok = True)