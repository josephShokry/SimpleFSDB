from abc import ABC, abstractmethod
from distutils.cmd import Command

from output.status import Status

"""the interface Icommand"""
class Icommand(ABC):
    def execute(self,status):
        if status == Status.SUCCESS:
           self.ExcuteInternal()
        else:
            return #an error message
    
    @abstractmethod                                          
    def isvalid(self):
        pass
    @abstractmethod 
    def ExcuteInternal(self):
        pass
