from abc import ABCMeta,  abstractstaticmethod

class Icommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute():
        """the interface Icommand"""