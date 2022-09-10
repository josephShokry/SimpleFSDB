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
import shutil, unittest, os, sys, json
from pickle import TRUE
from unittest.result import failfast
print(os.getcwd())
sys.path.append(os.path(str(os.getcwd()).replace("Test", '')))
print(os.getcwd())
from Source.Commands_Functions.schema_keys import Keys
from Source.Output.exceptions import *

parent_path = os.getcwd()

class test_functions(unittest.TestCase):
    def test_create_sch1(self):
        with open("testcases_schemas\sch1.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            #exceute the create command and make the DB
            changedir = parent_path
            os.system(changedir)
            cmd = "python main.py -cmd create -sch testcases_schemas\sch1.txt"
            os.system(cmd)
            #check if there is any problem
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch2(self):
        with open("testcases_schemas\sch2.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            changedir = parent_path
            os.system(changedir)
            cmd = "python main.py -cmd create -sch testcases_schemas\sch2.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch3(self):
        with open("testcases_schemas\sch3.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            changedir = parent_path
            os.system(changedir)
            cmd = "python main.py -cmd create -sch testcases_schemas\sch3.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_create_sch4(self):
        with open("testcases_schemas\sch4.txt","r") as schema_file:
            schema = json.load(schema_file)
            changedir = parent_path
            os.system(changedir)
            cmd = "python main.py -cmd create -sch testcases_schemas\sch4.txt"
            os.system(cmd)
            check = TRUE
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_create_5(self):#missing the schema
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create"
        try:
            os.system(cmd)
        except MissingInput:
            pass
    
    def test_create_6(self): #worng schema path
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch schemaa.txt"
        try:
            os.system(cmd)
        except WrongInput:
            return
        return failfast

    def test_create_7(self):#not valid schema file
        changedir = parent_path
        os.system(changedir)
        cmd = "python main.py -cmd create -sch testcases_schemas\sch5.txt"
        try:
            os.system(cmd)
        except WrongInput:
            pass
        return failfast
          

if __name__ == '__main__':
    unittest.main()