'''
important dont change the order of tests because the order has a meaning as some of the tests depend on previous tests
schemas
sch1 -> normal schema
sch2 -> create the DB beside there is a created one but there is a shortage int the tables
sch3 -> create beside a created DB
sch4 -> just the dir of the DB with no tables
//
test 5 -> missing schema path
sch5 -> wrong schema path
sch6 -> invalid schema json
sch7 -> 
'''
from pickle import TRUE
import shutil
import unittest
import os,sys
from unittest.result import failfast
import json



sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''),"source"))
from main import *
from commands_functions.schema_keys import Keys
from outputs.exceptions import *


main_path = os.path.join(os.getcwd(),"source")

class test_create_function(unittest.TestCase):
    def test_create_sch1(self):
        with open("tests\\testcases_schemas\sch1.txt", 'r')as schema_file:
            schema = json.load(schema_file)
            #exceute the create command and make the DB
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch1.txt"
            os.system(cmd)

            #check if there is any problem
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch2(self):
        with open("tests\\testcases_schemas\sch2.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch2.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch3(self):
        with open("tests\\testcases_schemas\sch3.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch3.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_create_sch4(self):
        with open("tests\\testcases_schemas\sch4.txt","r") as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch4.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_create_5(self):#missing the schema
        os.system(main_path)
        cmd = "python source\main.py -cmd create"
        try:
            os.system(cmd)
        except MissingInput:
            pass
    
    def test_create_6(self): #worng schema path
        os.system(main_path)
        cmd = "python source\main.py -cmd create -sch schemaa.txt"
        try:
            os.system(cmd)
        except WrongInput:
            return
        return failfast

    def test_create_7(self):#not valid schema file
        os.system(main_path)
        cmd = "python source\main.py -cmd create -sch testcases_schemas\sch5.txt"
        try:
            os.system(cmd)
        except WrongInput:
            pass
        return failfast
    

if __name__ == '__main__':
    unittest.main()