from Create_Command import CreateCommand
from Delete_Command import DeleteCommand
from Get_Command import GetCommand
from Set_Command import SetCommand
from output.exceptions import *
from output.status import Status

class CommandFactory:
    @staticmethod
    def create_commands(args):
        command_type = args.command
        if command_type == "create":
            return CreateCommand(args.schema_path)
        elif command_type == "delete":
            return DeleteCommand()
        elif command_type == "get":
            return GetCommand()
        elif command_type == "set":
            return SetCommand()
        else :
            raise WrongInput(status = Status.WrongInput, message = "wrong command")