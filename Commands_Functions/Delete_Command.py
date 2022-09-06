import os, json
from Commands_Functions.EnumStatus import Status
from Commands_Functions.Icommand import Icommand
from Schema_Keys import Keys

class DeleteCommand(Icommand):


    def isvalid(self):
        return Status.success
    def ExcuteInternal(self):
         print("dummy delete will be implemented later")
 