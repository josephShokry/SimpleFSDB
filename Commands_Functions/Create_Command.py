import os, json
from Schema_Keys import Keys
from I_Command import ICommand

class CreateCommand(ICommand):
    def __init__(self, schema_path):
        self.validate(schema_path)
    def validate(self, schema_path):
        if not os.path.exists(schema_path):
            print('schema path is incorrect')
            exit()
        self.schema_file = schema_path
        schema = open(schema_path, "r")
        try:
            self.schema_data = json.load(schema)
        except:
            print('schema is written in a wrong json format')
            exit()
        schema.close()
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
            
#ToDo: Handle input wrong schema path (line 8)