import os, json
from textwrap import indent
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
from outputs.status import Status



def writeToJSONFile(path, fileName, data):
        filePathNameWExt =  path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp,indent=2)
             

class CreateCommand(AbtractCommand):
    def __init__(self, schema_path):
        self.schema_data = CreateCommand.__validate(schema_path)

    @staticmethod  
    def __validate(schema_path):
        if schema_path == None:
            raise MissingInput(status = Status.MissingInput, message = "the schema is missing")
        if not os.path.exists(schema_path) :
            raise FileNotFound(status = Status.FileNotFound, message = "the schema path is not valid")
        with open(schema_path, 'r') as schema: 
            try:
                schema_data = json.load(schema)
            except:
                raise WrongInput(status = Status.WrongInput, message = "schema is written in a wrong json format")
        return schema_data

    def execute(self):
        parent_dir = os.getcwd() #get the current dir of the project
        database_name = self.schema_data[Keys.DB_NAME]
        path = os.path.join(parent_dir, database_name)
        os.makedirs(path, exist_ok = True)
        if not Keys.TABLES in self.schema_data:
            return
        for table in self.schema_data[Keys.TABLES]:
            table_path = os.path.join(path, table[Keys.NAME])
            os.makedirs(table_path, exist_ok = True)
            writeToJSONFile(table_path, "schema",table) # make file schema
            indices_path = os.path.join(table_path,"indices")# make indices folder
            os.makedirs(indices_path, exist_ok = True)
            for index in table[Keys.INDEX_KEY]: 
                ind_path = os.path.join(indices_path, index)
                os.makedirs(ind_path, exist_ok = True)