from abc import ABCMeta, abstractstaticmethod

class AbtractCommand(metaclass = ABCMeta):
    @abstractstaticmethod
    def execute():
        """the interface Icommand"""