from abc import ABCMeta,abstractclassmethod, abstractstaticmethod

class AbtractCommand(metaclass = ABCMeta):
    @abstractstaticmethod
    def execute():
        """the interface Icommand"""