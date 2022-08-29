import json
from multiprocessing.connection import wait
import Parser
import commands_function
import time


if __name__=='__main__':
    args=Parser.parseInput()
    command =commands_function.commandfactory.build_command(args)
    command.excute(args)

    # if args.command=="create":
    #     f=open(args.schema,"r")
    #     data=json.load(f)
    #     commands_function.create(data)

    # #all the comming functions and inputs are dummies they will be implemented later
    # elif args.command=="set":
    #     commands_function.set(5,3)
    # elif args.command=="delete":
    #     commands_function.delete(5)
    # elif args.command=="get":
    #     commands_function.get(5)
    