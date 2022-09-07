from abc import ABC, abstractmethod

from output.status import Status

"""the interface Icommand"""
class Icommand(ABC):
    @abstractmethod 
    def execute(self):
        pass
    
    @abstractmethod                                          
    def isvalid(self):
        pass