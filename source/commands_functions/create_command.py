import os, json
from textwrap import indent
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from models.database import Database
from outputs.exceptions import *
from outputs.status import Status



# def writeToJSONFile(path, fileName, data):
        # filePathNameWExt =  path + '/' + fileName + '.json'
        # with open(filePathNameWExt, 'w') as fp:
        #     json.dump(data, fp,indent=2)
             

class CreateCommand(AbtractCommand):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        CreateCommand.__validate(schema_path)
    @staticmethod  
    def __validate(schema_path):
        if schema_path == None:
            raise MissingInput(status = Status.MissingInput, message = "the schema is missing")
    
    def execute(self):
        database = Database(schema_path = self.schema_path)
        database.serialize()