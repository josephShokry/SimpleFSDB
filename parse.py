import argparse
import os
import string
from tokenize import String

parser = argparse.ArgumentParser(description="testing the parsing in python")
parser.add_argument('words',type=str,help="to parse the input and print it")
args=parser.parse_args()

if __name__=='__main__':
    print (args.words)