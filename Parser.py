import argparse

def parseInput():
    global parser
    parser=argparse.ArgumentParser()
    parser.add_argument("-cmd","--command",type=str)
    parser.add_argument("-sch","--schema",type=str)
    parser.add_argument("-pk","--primaryKey",type=str)
    parser.add_argument("-val","--value",type=str)  
    parser.add_argument("-dp","--data_base",type=str)
    parser.add_argument("-tb","--table",type=str)  
    

    return parser.parse_args() 

#not completed function
# def get_argument():
#     parser2=argparse.ArgumentParser(parents=[parser])
#     parser2.add_argument("-cmd","--command",type=str)
#     parser2.add_argument("-sch","--schema",type=str)
#     parser2.add_argument("-pk","--primaryKey",type=str)
#     parser2.add_argument("-val","--value",type=str)  
#     parser2.add_argument("-dp","--data_base",type=str)
#     parser2.add_argument("-tb","--table",type=str) 
#     parser=parser2
#     return parser2.parse_args()

#parent_parser = argparse.ArgumentParser