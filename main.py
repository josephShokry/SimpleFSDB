import json
from multiprocessing.connection import wait
import Parser
import commands_function
import time


if __name__=='__main__':
    args=Parser.parseInput()
    args2=args
    data= None

    if args.command=="create":
        #TODO check if the user entered the schema and if not ask him for it
        # while args.schema==None:
        #     print("please enter the name of schema text file")
        #     args2=Parser.parseInput()
        f=open(args.schema,"r")
        data=json.load(f)
        commands_function.create(data)

    #all the comming functions and inputs are dummies they will be implemented later
    elif args.command=="set":
        commands_function.set(5,3)
    elif args.command=="delete":
        commands_function.delete(5)
    elif args.command=="get":
        commands_function.get(5)
    