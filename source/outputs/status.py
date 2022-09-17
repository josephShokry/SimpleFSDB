from enum import Enum

class Status(Enum):
    Success = 0
    MissingInput = 1
    FileNotFound = 2
    WrongInput = 3
    TableNotExist = 4 
    RowExists = 5
    DatabaseNotExist = 6
    Primary_keyNotExist = 7
    ColumnsNotExistInSchema = 8