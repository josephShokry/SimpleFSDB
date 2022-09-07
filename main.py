import Parser, sys, os
from output.output import OutPut
from output.status import Status

sys.path.append(os.path.join(os.getcwd(), "Commands_Functions"))
from Commands_Functions.Command_Factory import CommandFactory

if __name__=='__main__':
    try:
        args = Parser.parseInput()
        command = CommandFactory.create_commands(args)
        status = command.isvalid()
        command.execute(status)
    except Exception as e:
        #excetpion_object = ExceptionFactory(type(e).__name__)
        #excetpion_object = ExceptionFactory.create_exception(type(e).__name__)
        #print(repr(excetpion_object))
        OutPut(status = e.status, message = e.message)

    else:
        OutPut(status = Status.SUCCESS)