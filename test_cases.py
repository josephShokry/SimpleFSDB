import unittest
import os
from schema_keys import keys
import json

parent_path = os.getcwd()

class test_functions(unittest.TestCase):
    schema_file = open("schema.txt", "r")
    global schima
    schima = json.load(schema_file)
    def test_create_DB(self):
        self.assertTrue(os.path.isdir(os.path.join(parent_path, schima[keys.DB_NAME])))
    def test_create_tables(self):
        parent_table_path=os.path.join(parent_path, schima[keys.DB_NAME])
        for table in schima[keys.TABLES]:
            self.assertTrue(os.path.isdir(os.path.join(parent_table_path, table[keys.NAME])))

if __name__=='__main__':
    #make sure to run the next command in cmd before running the test cases file
    #command="python main.py -cmd create -sch schema.txt"
    unittest.main()