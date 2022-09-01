import os
import json
from SchemaKeys import Keys
from Icommand import Icommand
        
class Create(Icommand):
    def __init__(self, schema_file):
        self.schema_file = schema_file
        try:
            schema = open(schema_file, "r")
        except:
            print('wrong schema path')
            return
        try:
            self.schema_data = json.load(schema)
        except:
            print('schema is written in a wrong json format')
            return
        schema.close()
    def execute(self):
        schema_data = self.schema_data
        parent_dir = os.getcwd() #get the current dir of the project
        data_base_name = schema_data[Keys.DB_NAME]
        path = os.path.join(parent_dir, data_base_name)
        if not os.path.isdir(path): #to check if the DB directory is created before or not
            os.mkdir(path, True)
        try:
            for table in schema_data[Keys.TABLES]:
                table_path = os.path.join(path, table[Keys.NAME])
                if not os.path.isdir(table_path):
                    os.mkdir(table_path, True)
                    # file_name = os.path.join(table_path, "info.txt")
                    # f = open(file_name, 'w')
                    # f.write(json.dumps(i,  indent = 4))
        except:
            print('No Tables Found')