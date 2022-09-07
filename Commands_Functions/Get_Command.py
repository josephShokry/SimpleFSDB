import os, json
from Commands_Functions.icommand import Icommand
from schema_keys import Keys
from output.status import Status

class GetCommand(Icommand):

    def isvalid(self):
        pass
    def execute(self):
        print("dummy get will be implemented later")