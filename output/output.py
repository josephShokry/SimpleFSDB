from output.status import Status

class OutPut:
    def __init__(self, result = None, message = None, status = None):
        if status == Status.SUCCESS:
            self.message = "the command has been executed successfully!"
        else:
            self.message = "the command has not been executed!\n" + message