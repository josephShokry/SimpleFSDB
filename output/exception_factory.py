from output.exceptions import *


class ExceptionFactory:
    def __init__(self, exception_name):
        if (exception_name == "DBNotFound"):
            return DBNotFound
        elif (exception_name == "TableNotFound"):
            return TableNotFound
        elif (exception_name == "MissingInput"):
            return MissingInput
        elif (exception_name == "FileNotFound"):
            return FileNotFound
        elif (exception_name == "WrongInput"):
            return WrongInput





