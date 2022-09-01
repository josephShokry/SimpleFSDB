from Icommand import Icommand
import os
import json
from SchemaKeys import Keys

class Create(Icommand):
    def __init__(self, schema):
        self.schema = schema
    def execute(self):
        schema = self.schema
        try:
            schema_file = open(schema, "r")
        except:
            print('wrong schema path')
            return
        try:
            schema = json.load(schema_file)
        except:
            print('schema is written in a wrong json format')
            return
        parent_dir = os.getcwd() #get the current dir of the project
        data_base_name = schema[Keys.DB_NAME]
        path = os.path.join(parent_dir, data_base_name)
        if not os.path.isdir(path): #to check if the DB directory is created before or not
            os.mkdir(path, True)
        try:
            for table in schema[Keys.TABLES]:
                table_path = os.path.join(path, table[Keys.NAME])
                if not os.path.isdir(table_path):
                    os.mkdir(table_path, True)
                    # file_name = os.path.join(table_path, "info.txt")
                    # f = open(file_name, 'w')
                    # f.write(json.dumps(i,  indent = 4))
        except:
            print('No Tables Found')
        schema_file.close()