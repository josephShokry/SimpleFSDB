from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def validate(schema_path):
        """the interface Icommand"""
    def execute():
        """the interface Icommand"""