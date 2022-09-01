import argparse

def parseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("-cmd", "--command", type = str.lower, help = "the quiry command", required = True, choices = ["get", "set", "create", "delete"])
    parser.add_argument("-sch", "--schema", type = str, required = (parser.parse_known_args()[0].command == "create"), help = "path to your schema file")
    parser.add_argument("-pk", "--primaryKey", type = str, help = "the primary key of the DB row you want to access")
    parser.add_argument("-val", "--value", type = str, help = "the value that you want to change or add to the DB")  
    parser.add_argument("-db", "--data_base", type = str, help = "the database name")
    parser.add_argument("-tb", "--table", type = str, help = "the table name that you want to access")  
    
    return parser.parse_args()