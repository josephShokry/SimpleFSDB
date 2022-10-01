from asyncio.windows_events import NULL
import shutil
import unittest,sys,os,json
sys.path.append(os.path.join(os.getcwd(),"source"))
from commands_functions.schema_keys import Keys
from commands_functions.get_command import *
from commands_functions.set_command import *
from commands_functions.delete_command import *
from outputs.exceptions import *
from outputs.output import *

class test_set_function(unittest.TestCase):

    def test_delete_1(self):# no error delete the value
        print('test # 1')
        DeleteCommand("csed2025", "Students", "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
        result = GetCommand("csed2025", "Students", "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
        output_object = outputs(result = result)  
        self.assertListEqual([], result)            
        print(json.dumps(output_object.__dict__, indent=2))

    def test_delete_2(self):# not enter the table 
        print('test # 2')
        try:
           result = DeleteCommand("csed2025",None, "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except TableNotExist as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_3(self):# not enter the database
        print('test # 3')
        try:
           result = DeleteCommand(None,"Students", "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except WrongInput as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_4(self):# Wrong database name
        print('test # 4')
        try:
           result = DeleteCommand("cssssssed2025","Students", "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except DatabaseNotExist as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_5(self):# Wrong table name 
        print('test # 5')
        try:
           result = DeleteCommand("csed2025","Studddddents", "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except TableNotExist as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_6(self):# enter a column doesn't exist in the table 
        print('test # 6')
        try:
           result = DeleteCommand("csed2025","Students", "{\"iiiid\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except ColumnsNotExistInSchema as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_7(self):# not valid json query 
        print('test # 7')
        try:
           result = DeleteCommand("csed2025","Students", "{\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
           output_object = outputs(result= result)
        except WrongInput as e:
           output_object = outputs(exception = e, result = None)
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_8(self):# the query has the primary key but wrong in other data
        print('test # 8')
        result = DeleteCommand("csed2025","Students", "{\"id\": \"5\",\"first_name\": \"joooooseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
        output_object = outputs(result= result)
        self.assertEqual(None,result)            
        print(json.dumps(output_object.__dict__,indent=2))

    def test_delete_9(self):# the query has index but not in the file
        print('test # 9')
        result = DeleteCommand("csed2025","Students", "{\"first_name\": \"joooooseph\",\"last_name\": \"shokry\",\"age\": \"20\"}").execute() 
        output_object = outputs(result= result)
        self.assertEqual(None,result)            
        print(json.dumps(output_object.__dict__,indent=2))
    
    def test_delete_10(self):# the query has much information than any value in the database
        print('test # 10')
        result = DeleteCommand("csed2025","Students", "{\"first_name\": \"joooseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute() 
        output_object = outputs(result= result)
        self.assertEqual(None,result)            
        print(json.dumps(output_object.__dict__,indent=2))

if __name__ == '__main__':
   main_path = os.getcwd()
   schema = None
   with open("tests\\testcases_schemas\schema.txt", 'r')as schema_file:
      schema = json.load(schema_file)
      os.system(main_path)
      cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\schema.txt"
      os.system(cmd)
   SetCommand("csed2025", "Students","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
   SetCommand("csed2025", "Students","{\"first_name\": \"joooseph\",\"last_name\": \"shokry\",\"age\": \"20\"}").execute()   
   SetCommand("csed2025", "Students","{\"id\": \"15\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
   unittest.main(exit=False)
   shutil.rmtree(os.path.join(main_path,schema[Keys.DATABASE_NAME]))