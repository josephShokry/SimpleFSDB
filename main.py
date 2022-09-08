import argparse
import parsing, sys, os, json
from output.output import Output
from output.status import Status

sys.path.append(os.path.join(os.getcwd(), "Commands_Functions"))
from Commands_Functions.command_factory import CommandFactory

if __name__=='__main__':
    result = None
    try:
        args = parsing.parseInput()
        command = CommandFactory.create_commands(args)
        result = command.execute()
        output_object = Output(result)
    except Exception as e:
       output_object = Output(e,result)
    print(json.dumps(output_object.__dict__, indent = 2)) 



 