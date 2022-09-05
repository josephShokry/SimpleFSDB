import Parser, sys, os
sys.path.append(os.path.join(os.getcwd(), "Commands_Functions"))
from Commands_Functions.Command_Factory import CommandFactory

if __name__=='__main__':
    args = Parser.parseInput()
    command = CommandFactory.create(args)
    status = command.isvalid()
    command.execute(status)
