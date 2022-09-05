from abc import ABC, abstractmethod
from distutils.cmd import Command

"""the interface Icommand"""
class Icommand(ABC):
    def execute(self,status):
        if status == "success":
           self.ExcuteInternal()
        else:
            return #an error message
    
    @abstractmethod                                          
    def isvalid(self):
        pass
    @abstractmethod 
    def ExcuteInternal(self):
        pass
