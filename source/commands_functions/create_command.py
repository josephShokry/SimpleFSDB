from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from models.database import Database
from outputs.exceptions import *
from outputs.status import Status
import os, json



class CreateCommand(AbtractCommand):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.schema_data = self.__validate_schema_path(schema_path)

    def execute(self):
        database = Database(schema_data = self.schema_data)
        database.serialize()
    
    @staticmethod
    def __validate_schema_path(schema_path):
        if schema_path == None:
            raise MissingInput(status = Status.MissingInput, message = "the schema is missing")

        if not os.path.exists(schema_path) :
            raise FileNotFound(status = Status.FileNotFound, message = "the schema path is not valid")
        with open(schema_path, 'r') as schema_file: 
            try:
                schema_data = json.load(schema_file)
            except:
                raise WrongInput(status = Status.WrongInput, message = "schema is written in a wrong json format")
        return schema_data