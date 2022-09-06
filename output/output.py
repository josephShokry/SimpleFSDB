from sre_constants import SUCCESS
from status import Status
class OutPut:
    def __init__(self, result = None, message = None, status = None):
        if status == Status.SUCCESS:
            print("the command has been executed successfully!")
        else:
            print("the command has not been executed")
            print(message)
    