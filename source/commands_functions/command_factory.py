from commands_functions.create_command import *
from commands_functions.delete_command import *
from commands_functions.get_command import *
from commands_functions.set_command import *
from outputs.exceptions import *
from outputs.status import Status

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
            return SetCommand(args.data_base, args.table, args.value)
        else :
            raise WrongInput(status = Status.WrongInput, message = "wrong command")