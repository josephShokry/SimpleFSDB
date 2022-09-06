from Create_Command import CreateCommand
from Delete_Command import DeleteCommand
from Get_Command import GetCommand
from Set_Command import SetCommand
from output.exceptions import MissingInput
from output.status import Status

class CommandFactory:
    @staticmethod
    def create_commands(args):
        command_type = args.command
        if command_type == "create":
            if(args.schema_path == None):
                #the parameter are for test not final
                raise MissingInput(status=Status.MissingInput, message = "hi joe")
            return CreateCommand(args.schema_path)
        elif command_type == "delete":
            return DeleteCommand()
        elif command_type == "get":
            return GetCommand()
        elif command_type == "set":
            return SetCommand()