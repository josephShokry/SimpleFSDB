from enum import Enum

class Status(Enum):
    Success = 0
    DBNotFound = 1
    TableNotFound = 2
    MissingInput = 3
    FileNotFound = 4
    WrongInput = 5
    TableNotExist = 6 
    RowExists = 7
    DatabaseNotExist = 8
    Primary_keyNotExist = 9
    ColumnsNotExistInSchema = 10