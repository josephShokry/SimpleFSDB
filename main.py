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
    except Exception as e:
       output_object = Output(e,result)
    else:
        output_object = Output(result)

    output_josn = output_object.output_json()
    print(json.dumps(output_josn, indent = 2)) 



 