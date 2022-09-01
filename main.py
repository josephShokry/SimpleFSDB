import Parser
import sys, os
sys.path.append(os.path.join(os.getcwd(), "CommandsFunctions"))
from CommandsFunctions.CommandFactory import CommandFactory

if __name__=='__main__':
    args = Parser.parseInput()
    command = CommandFactory.build_command(args)
    command.execute()