import argparse
import os

parser = argparse.ArgumentParser()
parent_path=os.getcwd()
def parseInput():
    parser=argparse.ArgumentParser()
    parser.add_argument("-cmd","--command",type=str)
    parser.add_argument("-sch","--schema",type=str)  
    if(parser.parse_known_args()[0].command=="create"and 
    (parser.parse_known_args()[0].schema==None or #if the user forgot to parse the schema file
    not os.path.isdir(os.path.join(parent_path,parser.parse_known_args()[0].schema)))): #if the user parse a not existent file
        print("please enter a valid query")
        parser.add_argument("sch",type=str)    
    parser.add_argument("-pk","--primaryKey",type=str)
    parser.add_argument("-val","--value",type=str)  
    parser.add_argument("-dp","--data_base",type=str)
    parser.add_argument("-tb","--table",type=str)  
    

    return parser.parse_args() 