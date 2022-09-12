import os, json
from commands_functions.abstract_command import AbtractCommand
from commands_functions.schema_keys import Keys
from outputs.exceptions import *
 
class SetCommand(AbtractCommand):
    def __init__(self, data_base_name, table_name, value, disableoverwrite):
       '''
        - json file objecte will created in the validate its name is the pk and pares it here to an object file 
        - then the execute will take the parsed file object and the parsed json value and will write the values of the (value)
       in the file 
        - then will update the indices
       ''' 
       self.json_obj = self.__validate(data_base_name, table_name, value, disableoverwrite)

    @staticmethod  
    def __validate(data_base_name, table_name, value, disableoverwrite):
        '''
        - DB exist
        - table exist 
        - value not a valid json
        - value pk is missing 
        - row exist
        - coloumn exist
        - value is not compatible with the schema of the table
        '''
        valuee = '{"id":"5" ,"first_name":"joseph", "last_name": "shokry","age":"20", "gender":"male","ali":"j"}'
        val = eval(valuee)
        if data_base_name == None or table_name == None or value == None:
            raise WrongInput(message = "missing some inputs")

        #the current directory now is the source folder
        if not os.path.isdir(data_base_name):
            raise DatabaseNotExist()

        if not os.path.exists(data_base_name + "\\" + table_name):
            raise TableNotExist()

        # try:
        #     print(val)
        #     print(type(val))
        #     json_obj = json.loads(val)
        # except:
        #     raise WrongInput(message = "The value json text is invalid")
        
        json_obj = val
        if "id"  not in json_obj:
            raise WrongInput(message = "The value json text is invalid, it has not any id parameter")

        if disableoverwrite and os.path.exists(data_base_name + "\\" + table_name + "\\" + json_obj["id"]):
            raise RowExists()

        with open(data_base_name + "\\" + table_name + "\\" + "schema.json", 'r') as table_schema_file: 
            try:
                table_schema_obj = json.load(table_schema_file)
            except:
                raise WrongInput(status = Status.WrongInput, message = "table schema is not found")

        for column in json_obj:
            if column not in table_schema_obj["columns"]:
                raise ColumnsNotExistInSchema(message = column + " coloumn is not exist in the table schema")
        
        return json_obj
        

        

    def execute(self):
        # mk_new_file()
        # update_indices()
        pass


'''
python main.py -cmd set -db csed2025 -tb Students -val
'''
'''
"'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'"
'''