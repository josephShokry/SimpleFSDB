from create_command import CreateCommand
from delete_command import DeleteCommand
from get_command import GetCommand
from set_command import SetCommand
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