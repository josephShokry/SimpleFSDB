from enum import Enum


class Status(Enum):
    SUCCESS = 0
    DBNotFound = 1
    TableNotFound = 2
    MissingInput = 3
    FileNotFound = 4
    WrongInput = 5