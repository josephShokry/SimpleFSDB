import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.status import Status

class GetCommand(AbtractCommand):

    def execute(self):
        print("dummy get will be implemented later")