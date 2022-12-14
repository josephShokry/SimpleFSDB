import shutil
import unittest,sys,os,json
sys.path.append(os.path.join(os.getcwd(),"source"))
from commands_functions.schema_keys import Keys
from commands_functions.set_command import SetCommand
from outputs.exceptions import *
from outputs.output import *

class test_set_function(unittest.TestCase):   
   def test_set_1(self): # set a row
      print('test # 1')
      try:
         result = SetCommand("csed2025", "Students","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except RowExists as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_2(self):# not giving the database name
      print('test # 2')
      try:
         result = SetCommand(None, "Students","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except WrongInput as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_3(self):# not giving the table name
      print('test # 3')
      try:
         result = SetCommand("csed2025",None,"{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except TableNotExist as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_4(self):# not giving the value
      print('test # 4')
      try:
         result = SetCommand("csed2025", "Students",None,).execute()   
         output_object = outputs(result)
      except WrongInput as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_5(self):# giving wrong db name or db not exist
      print('test # 5')
      try:
         result = SetCommand("cssssed2025", "Students","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except DatabaseNotExist as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))
   
   def test_set_6(self):# giving wrong table name or table not exist
      print('test # 6')
      try:
         result = SetCommand("csed2025", "Studeeenttts","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except TableNotExist as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_7(self):# the givin value does not have id coloumn
      print('test # 7')
      result = SetCommand("csed2025", "Students","{\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
      output_object = outputs(result)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_8(self):# miss match of the coloumns of the value with the table schema
      print('test # 8')
      try:
         result = SetCommand("csed2025", "Students","{\"id\": \"5\",\"firrrrrrst_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}").execute()   
         output_object = outputs(result)
      except ColumnsNotExistInSchema as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   def test_set_9(self): # set a row with same pk and overwrite is false
      print('test # 9')
      try:
         result = SetCommand("csed2025", "reservation","{\"id\": \"5\",\"fname\": \"joseph\",\"lname\": \"shokry\",\"age\": \"20\"}").execute()  
         result = SetCommand("csed2025", "reservation","{\"id\": \"5\",\"fname\": \"joseph\",\"lname\": \"shokry\",\"age\": \"20\"}").execute()    
         output_object = outputs(result)
      except RowExists as e:
         output_object = outputs(exception = e, result = None)
      print(json.dumps(output_object.__dict__, indent = 2))

   ## will be uncommented after the implementaion of the get
   # def test_set_12(self): # set a row with same pk and overwrite is true
   #    print('test # 12')
   #    result = SetCommand("csed2025", "Students","{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"female\"}").execute()  
   #    check = True
   #    self.assertFalse()
   #    output_object = outputs(result)
   #    print(json.dumps(output_object.__dict__, indent = 2))
   
if __name__ == '__main__':
   main_path = os.getcwd()
   schema = None
   with open("tests\\testcases_schemas\schema.txt", 'r')as schema_file:
      schema = json.load(schema_file)
      os.system(main_path)
      cmd = "python source\main.py -cmd create -sch tests\\testcases_schemas\schema.txt"
      os.system(cmd)
   unittest.main(exit=False)
   shutil.rmtree(os.path.join(main_path,schema[Keys.DATABASE_NAME]))