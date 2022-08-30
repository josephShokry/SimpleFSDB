import unittest
import os
from keys import keys
import json

parent_path=os.getcwd()

class test_functions(unittest.TestCase):
    f=open("schema.txt","r")
    global schima
    schima=json.load(f)
    def test_create_DB(self):
        self.assertTrue(os.path.isdir(os.path.join(parent_path,schima[keys.DB_name])))
    def test_create_tables(self):
        parent_table_path=os.path.join(parent_path,schima[keys.DB_name])
        for table in schima[keys.tables]:
            self.assertTrue(os.path.isdir(os.path.join(parent_table_path,table[keys.name])))

if __name__=='__main__':
    #make sure to run the next command in cmd before running the test cases file
    #command="python main.py -cmd create -sch schema.txt"
    unittest.main()