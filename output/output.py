from output.status import Status

class Output:
    def __init__(self,exception = None, result = None):

        if exception != None:
            self.message = exception.message
            self.status =  Status.printName(exception.status)
        else :
            self.message = "the command has been executed successfully!"
            self.status = Status.printName(Status.SUCCESS)
        self.json_obj = {"status": self.status, "message": self.message, "result": result}

    def output_json(self):
        return self.json_obj