
import shutil
import unittest,sys,os,json
sys.path.append(os.path.join(os.getcwd(),"source"))
from commands_functions.schema_keys import Keys
from commands_functions.create_command import CreateCommand
from outputs.exceptions import *
from outputs.output import *


main_path = os.path.join(os.getcwd(),"source")

class test_create_function(unittest.TestCase):
    def test_create_sch1(self):
        print('test # 1')
        with open("tests\\testcases_schemas\sch1.txt", 'r')as schema_file:
            schema = json.load(schema_file)
            #exceute the create command and make the DB
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch1.txt"
            os.system(cmd)

            #check if there is any problem
            check = True
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch2(self):
        print('test # 2')
        with open("tests\\testcases_schemas\sch2.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch2.txt"
            os.system(cmd)
            check = True
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            self.assertTrue(check)

    def test_create_sch3(self):
        print('test # 3')
        with open("tests\\testcases_schemas\sch3.txt", 'r') as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch3.txt"
            os.system(cmd)
            check = True
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_create_sch4(self):
        print('test # 4')
        with open("tests\\testcases_schemas\sch4.txt","r") as schema_file:
            schema = json.load(schema_file)
            parent_path = main_path.replace("\source","")
            os.system(main_path)
            cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\sch4.txt"
            os.system(cmd)
            check = True
            check = os.path.isdir(os.path.join(parent_path, schema[Keys.DB_NAME]))
            parent_table_path = os.path.join(parent_path, schema[Keys.DB_NAME])
            for table in schema[Keys.TABLES]:
                check = os.path.isdir(os.path.join(parent_table_path, table[Keys.NAME]))
            shutil.rmtree(os.path.join(parent_path,schema[Keys.DB_NAME]))
            self.assertTrue(check)

    def test_set_5(self):# missing the schema
        print('test # 5')
        try:
           result = CreateCommand(None).execute()   
           output_object = outputs(result)
        except MissingInput as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__, indent = 2))

    def test_set_6(self):# worng schema path
        print('test # 6')
        try:
           result = CreateCommand(schema_path="schemaa.txt").execute()   
           output_object = outputs(result)
        except FileNotFound as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__, indent = 2))

    def test_set_7(self):# not valid schema file
        print('test # 7')
        try:
           result = CreateCommand("tests\testcases_schemas\sch5.txt").execute()   
           output_object = outputs(result)
        except FileNotFound as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__, indent = 2))
    

if __name__ == '__main__':
    unittest.main(exit=False)