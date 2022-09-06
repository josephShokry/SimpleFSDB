import Parser, sys, os
from output.exception_factory import ExceptionFactory
from output.output import OutPut
from output.status import Status

sys.path.append(os.path.join(os.getcwd(), "Commands_Functions"))
from Commands_Functions.Command_Factory import CommandFactory

if __name__=='__main__':
    try:
        args = Parser.parseInput()
        command = CommandFactory.create(args)
        command.execute()
    except Exception as e:
        excetpion_object = ExceptionFactory(type(e).__name__)
        OutPut(status = excetpion_object.status, message = excetpion_object.message)
    else:
        OutPut(status = Status.SUCCESS)
