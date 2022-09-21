import unittest, os, sys
pa = os.getcwd()
p1 = os.path.join(os.path.dirname(__file__),"..")
p2 = os.pardir
root_dir = os.path.abspath(os.path.join(p1, "source"))
sys.path.append(root_dir)

from outputs.exceptions import *
# sys.path.append(pa)

main_path = os.path.join(os.getcwd(),"source")

class test_set_function(unittest.TestCase):
    def test_set_1(self):# not giving the database name
        os.system(main_path)
        cmd = "python source\main.py -cmd set"
        try:
            os.system(cmd)
        except e:
            self.assertEqual(e,WrongInput)
            pass
        
    def test_set_2(self):# not giving the table name
        os.system(main_path)
        cmd = "python source\main.py -cmd set -db csed2025"
        try:
            os.system(cmd)
        except WrongInput:
            pass
  
    def test_set_3(self):# not giving the value 
        os.system(main_path)
        cmd = "python source\main.py -cmd set -db sced2025 -tb Student"
        try:
            os.system(cmd)
        except WrongInput:
            pass

    def test_set_4(self):# giving wrong db name or db not exist
        os.system(main_path)
        cmd = "python main.py -cmd set -db cseddd2025 -tb Students -val "'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'""
        try:
            os.system(cmd)
        except DatabaseNotExist:
            pass
    
    def test_set_5(self):# giving wrong table name or table not exist
        os.system(main_path)
        cmd = "python main.py -cmd set -db csed2025 -tb Studenttts -val "'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'""
        try:
            os.system(cmd)
        except TableNotExist:
            pass

    #not implemented yet as i hard coded the value

    def test_set_6(self):# the givin value does not have id coloumn
        os.system(main_path)
        cmd = "python main.py -cmd set -db csed2025 -tb Students -val "'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'""
        try:
            os.system(cmd)
        except DatabaseNotExist:
            pass

    def test_set_7(self):# row exist and disable overwrite is ture 
        os.system(main_path)
        cmd = 'python main.py -cmd set -db csed2025 -tb Students -val "{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}"'
        with self.assertRaises(RowExists):
            os.system(cmd)
        # self.assertRaises(RowExists, os.system(cmd))
        # try:os.system(cmd)
        # except e:
        #     self.assertEqual(e, RowExists)
        #     pass

    # not implemented yet as i hard coded the value
    def test_set_8(self):# miss match of the coloumns of the value with the table schema
        os.system(main_path)
        cmd = "python main.py -cmd set -db csed2025 -tb Studenttts -val "'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'""
        try:
            os.system(cmd)
        except TableNotExist:
            pass
    
    # def test_set_9(self):#make new row no dublicate PK no dublicate index
    #     os.system(main_path)
    #     cmd = "python main.py -cmd set -db csed2025 -tb Studenttts -val "'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'""
    # def test_set_10(self):#make new row with dublicate PK with disable over write

    # def test_set_11(self):#make new row with dublicate PK with  over write

    # def test_set_12(self):#make new row no dublicate PK  dublicate index

        

if __name__ == '__main__':
    unittest.main()