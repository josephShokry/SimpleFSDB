import os, json
from Schema_Keys import Keys
from Icommand import Icommand

class CreateCommand(Icommand):
    def __init__(self, schema_file):
        self.schema_file = schema_file
        schema = open(schema_file, "r")
        try:
            self.schema_data = json.load(schema)
        except:
            print('schema is written in a wrong json format')
            exit()
        schema.close()



    #required to implement
    def isvalid(self):
        return "success"


    def ExcuteInternal(self):
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