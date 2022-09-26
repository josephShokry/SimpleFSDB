import os, json
from commands_functions.abstract_command import AbtractCommand
from outputs.exceptions import *
from models.table import *
from models.index import Index;
from models.database import Database

class SetCommand(AbtractCommand):
    def __init__(self, database_name, table_name, value):
        self.value_object = self.__validate_value(value = value)
        self.database_name = database_name
        self.table_name = table_name 
        
    def execute(self):
        database = Database(database_name = self.database_name)
        database.set(table_name = self.table_name, row = self.value_object)

    @staticmethod
    def __validate_value(value):
        try:
            json_obj = json.loads(value)
        except:
            raise WrongInput(message = "the value json in not valid")
        return json_obj
