from outputs.status import Status

class MissingInput(Exception):
    def __init__(self, status = Status.MissingInput, message = "There is a missed required input"):
        self.status = status.name
        super().__init__(message)
         
class DBNotFound(Exception):
    def __init__(self, status = Status.DBNotFound, message = "The DB is not found"):
        self.status = status.name
        super().__init__(message)
         
class TableNotFound(Exception):
    def __init__(self, status = Status.TableNotFound, message = "The table is not found"):
        self.status = status.name
        super().__init__(message)        

class FileNotFound(Exception):
    def __init__(self, status = Status.FileNotFound, message = "The file is not found"):
        self.status = status.name
        super().__init__(message)        
         
class WrongInput(Exception):
    def __init__(self, status = Status.WrongInput , message = "Wrong input"):
        self.status = status.name
        super().__init__(message)
    
class TableNotExist(Exception):
    def __init__(self, status = Status.TableNotExist , message = "The table is not exist"):
        self.status = status.name
        super().__init__(message)

class RowExists(Exception):
    def __init__(self, status = Status.RowExists , message = "Row is already exist"):
        self.status = status.name
        super().__init__(message)

class DatabaseNotExist(Exception):
    def __init__(self, status = Status.DatabaseNotExist , message = "Database is not exist"):
        self.status = status.name
        super().__init__(message)

class Primary_keyNotExist(Exception):
    def __init__(self, status = Status.Primary_keyNotExist , message = "Primary key is not exist"):
        self.status = status.name
        super().__init__(message)

class ColumnsNotExistInSchema(Exception):
    def __init__(self, status = Status.ColumnsNotExistInSchema , message = "The cloumn is not exist"):
        self.status = status.name
        super().__init__(message)