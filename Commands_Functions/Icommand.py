from abc import ABC, abstractmethod

class Icommand(ABC):
    @abstractmethod
    def execute():
        """the interface Icommand"""