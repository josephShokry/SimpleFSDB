import parsing, json
from Output.output import Output
from Commands_Functions.command_factory import CommandFactory

if __name__=='__main__':
    try:
        args = parsing.parseInput()
        command = CommandFactory.create_commands(args)
        result = command.execute()
        output_object = Output(result)
    except Exception as e:
       output_object = Output(exception = e, result = None)
    print(json.dumps(output_object.__dict__, indent = 2))