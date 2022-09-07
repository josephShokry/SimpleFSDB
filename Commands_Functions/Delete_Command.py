import os, json
from Commands_Functions.Icommand import Icommand
from Schema_Keys import Keys
from output.status import Status

class DeleteCommand(Icommand):


    def isvalid(self):
        return Status.SUCCESS
    def ExcuteInternal(self):
         print("dummy delete will be implemented later")
 