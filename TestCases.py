'''
important dont change the order of tests because the order has a meaning as some of the tests depend on previous tests
schemas
sch1 -> normal schema
sch2 -> create the DB beside there is a created one but there is a shortage int the tables
sch3 -> create beside a created DB
sch4 -> just the dir of the DB with no tables
//
sch5 -> wrong schema path
sch6 -> invalid schema json
sch7 -> 
'''
from pickle import TRUE
import shutil
import unittest
import os
from SchemaKeys import SchemaKeys
import json

parent_path = os.getcwd()

class test_functions(unittest.TestCase):
    def test_create_sch1(self):
        schema_file = open("testcases_schemas\sch1.txt","r")
        schema = json.load(schema_file)
        #exceute the create command and make the DB
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch testcases_schemas\sch1.txt"
        os.system(cmd)
        #check if there is any problem
        check = TRUE
        check = os.path.isdir(os.path.join(parent_path, schema[SchemaKeys.DB_NAME]))
        parent_table_path = os.path.join(parent_path, schema[SchemaKeys.DB_NAME])
        for table in schema[SchemaKeys.TABLES]:
            check = os.path.isdir(os.path.join(parent_table_path, table[SchemaKeys.NAME]))
        self.assertTrue(check)

    def test_create_sch2(self):
        schema_file = open("testcases_schemas\sch2.txt","r")
        schema = json.load(schema_file)
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch testcases_schemas\sch2.txt"
        os.system(cmd)
        check = TRUE
        check = os.path.isdir(os.path.join(parent_path, schema[SchemaKeys.DB_NAME]))
        parent_table_path = os.path.join(parent_path, schema[SchemaKeys.DB_NAME])
        for table in schema[SchemaKeys.TABLES]:
            check = os.path.isdir(os.path.join(parent_table_path, table[SchemaKeys.NAME]))
        self.assertTrue(check)

    def test_create_sch3(self):
        schema_file = open("testcases_schemas\sch3.txt","r")
        schema = json.load(schema_file)
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch testcases_schemas\sch3.txt"
        os.system(cmd)
        check = TRUE
        check = os.path.isdir(os.path.join(parent_path, schema[SchemaKeys.DB_NAME]))
        parent_table_path = os.path.join(parent_path, schema[SchemaKeys.DB_NAME])
        for table in schema[SchemaKeys.TABLES]:
            check = os.path.isdir(os.path.join(parent_table_path, table[SchemaKeys.NAME]))
        shutil.rmtree(os.path.join(parent_path,schema[SchemaKeys.DB_NAME]))
        self.assertTrue(check)

    def test_create_sch4(self):
        schema_file = open("testcases_schemas\sch4.txt","r")
        schema = json.load(schema_file)
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch testcases_schemas\sch4.txt"
        os.system(cmd)
        check = TRUE
        check = os.path.isdir(os.path.join(parent_path, schema[SchemaKeys.DB_NAME]))
        parent_table_path = os.path.join(parent_path, schema[SchemaKeys.DB_NAME])
        for table in schema[SchemaKeys.TABLES]:
            check = os.path.isdir(os.path.join(parent_table_path, table[SchemaKeys.NAME]))
        shutil.rmtree(os.path.join(parent_path,schema[SchemaKeys.DB_NAME]))
        self.assertTrue(check)

if __name__ == '__main__':
    #make sure to run the next command in cmd before running the test cases file
    #dir = "cd Desktop\check in system\DB\SimpleFSDB"
    #cmd = "python main.py -cmd create -sch schema.txt"
    unittest.main()
