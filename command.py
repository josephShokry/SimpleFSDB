from asyncio.windows_events import NULL
import imp
import json
import argparse
from re import A
import commands


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-cmd","--command",type=str)
    parser.add_argument("-sch","--schema",type=str)
    args=parser.parse_args() 
    if(args.schema is not None):
        data=json.loads(args.schema)

    if args.command=="create":
        commands.create(data)
    elif args.command=="set":
        commands.set(5,3)
    elif args.command=="delete":
        commands.delete(5)
    elif args.command=="get":
        commands.get(5)
    






'''
"{\"fname\": \"joseph\",\"lname\": \"shokry\",\"age\": 32}"
'''