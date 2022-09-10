from Commands_Functions.create_command import CreateCommand
from Commands_Functions.delete_command import DeleteCommand
from Commands_Functions.get_command import GetCommand
from Commands_Functions.set_command import SetCommand
from Output.exceptions import *
from Output.status import Status

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