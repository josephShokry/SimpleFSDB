import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.status import Status
 
class SetCommand(AbtractCommand):

    def execute(self):
        print("dummy set will be implemented later")