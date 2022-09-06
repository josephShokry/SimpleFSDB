from output.status import Status

class MissingInput(Exception):
    status = Status.MissingInput
    message = "there is a missed required input"
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(self.message)

class DBNotFound(Exception):
    def __init__(self, status = Status.DBNotFound, message = "The DB is not found"):
        self.status = status
        self.message = message
        super().__init__(self.message)

class TableNotFound(Exception):
    def __init__(self, status = Status.TableNotFound, message = "The table is not found"):
        self.status = status
        self.message = message
        super().__init__(self.message)

class FileNotFound(Exception):
    def __init__(self, status = Status.FileNotFound, message = "The file is not found"):
        self.status = status
        self.message = message
        super().__init__(self.message)

class WrongInput(Exception):
    def __init__(self, status = Status.WrongInput, message = "wrong input"):
        self.status = status
        self.message = message
        super().__init__(self.message)
