import os, json
from Commands_Functions.abstract_command import AbtractCommand
from Commands_Functions.schema_keys import Keys
from outputs.status import Status

class GetCommand(AbtractCommand):

    def execute(self):
        print("dummy get will be implemented later")