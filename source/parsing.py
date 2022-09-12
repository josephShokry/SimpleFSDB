import argparse

def  parseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("-cmd", "--command", type = str.lower, help = "the quiry command", required = True)
    parser.add_argument("-sch", "--schema_path", type = str,help = "path to your schema file")
    parser.add_argument("-pk", "--primaryKey", type = str, help = "the primary key of the DB row you want to access")
    parser.add_argument("-val", "--value", type = str, help = "the value that you want to change or add to the DB")  
    parser.add_argument("-db", "--data_base", type = str, help = "the database name")
    parser.add_argument("-tb", "--table", type = str, help = "the table name that you want to access")
    parser.add_argument("-dow", "--disableoverwrite", type = bool, default = True, help = "when it is true it will over write in the stored row, if it isn't it will raise exception if the row is already exist")
    return parser.parse_args()

    