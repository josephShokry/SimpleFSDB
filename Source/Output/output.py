from Output.status import Status

class Output:
    def __init__(self,exception = None, result = None):
        self.result = result
        if exception != None:
            self.message = str(exception)
            self.status =  exception.status
        else :
            self.message = "the command has been executed successfully!"
            self.status = Status.Success.name