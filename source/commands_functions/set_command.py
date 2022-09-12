import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.status import Status
 
class SetCommand(AbtractCommand):
    def __init__(self):
       '''
        - json file objecte will created in the validate its name is the pk and pares it here to an object file 
        - then the execute will take the parsed file object and the parsed json value and will write the values of the (value)
       in the file 
        - then will update the indices
       ''' 

    @staticmethod  
    def __validate():
        '''
        - DB exist
        - table exist 
        - row exist
        - coloumn exist
        - value not a valid json
        - value is not compatible with the schema of the table
        - value pk is missing 
        '''
        
        

    def execute(self):
        print("dummy set will be implemented later")