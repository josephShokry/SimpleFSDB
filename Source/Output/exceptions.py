from Output.status import Status

class MissingInput(Exception):
    def __init__(self, status = Status.MissingInput, message = "there is a missed required input"):
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
    def __init__(self, status = Status.WrongInput , message = "wrong input"):
        self.status = status.name
        super().__init__(message)