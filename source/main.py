import parsing, json
from outputs.output import outputs
from commands_functions.command_factory import CommandFactory

if __name__=='__main__':
    try:
        args = parsing.parseInput()
        command = CommandFactory.create_commands(args)
        result = command.execute()
        output_object = outputs(result)
    except Exception as e:
       output_object = outputs(exception = e, result = None)
    print(json.dumps(output_object.__dict__, indent = 2))