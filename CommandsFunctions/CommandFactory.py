from Create import Create
from Delete import Delete
from Get import Get
from Set import Set

class CommandFactory:
    @staticmethod
    def build_command(args):
        command_type=args.command
        if command_type == "create":
            return Create(args.schema_file)
        elif command_type == "delete":
            return Delete()
        elif command_type == "get":
            return Get()
        elif command_type == "set":
            return Set()