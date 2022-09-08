import parser, sys, os, json
from output.output import OutPut
from output.status import Status

sys.path.append(os.path.join(os.getcwd(), "Commands_Functions"))
from Commands_Functions.command_factory import CommandFactory

if __name__=='__main__':
    try:
        args = parser.parseInput()
        command = CommandFactory.create_commands(args)
        command.execute()
    except Exception as e:
        output_message = OutPut(status = e.status, message = e.message)
    else:
        output_message = OutPut(status = Status.SUCCESS)

print(output_message.message)