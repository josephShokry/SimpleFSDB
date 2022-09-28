import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.exceptions import WrongInput
from outputs.status import Status
from models.database import Database
 

class GetCommand(AbtractCommand):
    
    def __init__(self, database_name, table_name, query): # we should check that db , tb isnot none
        self.database_name = database_name
        self.table_name = table_name
        if query is None or query.isspace() or not len(query):
            query = "{}"
        try:
            self.query = json.loads(query)
        except:
            raise WrongInput(message = "the query json in not valid")
 
    def execute(self):
        database = Database(database_name=self.database_name)
        return database.get(self.table_name, self.query)