import os, json
from commands_functions.abstract_command import AbtractCommand
from outputs.exceptions import *
from models.table import *
from models.index import Index;

class SetCommand(AbtractCommand):
    def execute(self):
        print("dummy get will be implemented later")