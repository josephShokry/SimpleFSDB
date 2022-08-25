import json
import argparse
import commands

def parseInput():
    parser=argparse.ArgumentParser()
    parser.add_argument("-cmd","--command",type=str)
    parser.add_argument("-sch","--schema",type=str)
    parser.add_argument("-pk","--primaryKey",type=str)
    parser.add_argument("-val","--value",type=str)  
      
    return parser.parse_args() 


if __name__=='__main__':
    args=parseInput()
    data= None
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