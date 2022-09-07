import os, json
from schema_keys import Keys
from icommand import Icommand
from output.exceptions import MissingInput, WrongInput
from output.status import Status

class CreateCommand(Icommand):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.isvalid()
        
    def isvalid(self):
        if self.schema_path == None or not os.path.exists(self.schema_path) :
            raise MissingInput(status = Status.MissingInput, message = "the schema is missing")
        self.schema_file = self.schema_path
        with open(self.schema_path, 'r') as schema: 
            try:
                self.schema_data = json.load(schema)
            except:
                raise WrongInput(status = Status.WrongInput, message = "schema is written in a wrong json format")

    def execute(self):
        schema_data = self.schema_data
        parent_dir = os.getcwd() #get the current dir of the project
        data_base_name = schema_data[Keys.DB_NAME]
        path = os.path.join(parent_dir, data_base_name)
        os.makedirs(path, exist_ok = True)
        if not Keys.TABLES in schema_data:
            return
        for table in schema_data[Keys.TABLES]:
            table_path = os.path.join(path, table[Keys.NAME])
            os.makedirs(table_path, exist_ok = True)
            
