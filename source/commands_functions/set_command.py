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
       self.path = data_base_name + "\\" + table_name

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
        valuee = '{"id":"5" ,"first_name":"joseph", "last_name": "shokry","age":"20", "gender":"male"}'

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

        if disableoverwrite and os.path.exists(data_base_name + "\\" + table_name + "\\" + json_obj["id"] + ".json"):
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
        

    def mk_new_file(self):
        json_data = json.dumps(self.json_obj, indent = 2)
        with open(self.path + "//" + self.json_obj["id"] + ".json", 'w') as row_file: 
            row_file.write(json_data)

    def update_indices(self):
        table_schema_file = open(self.path + "\\" + "schema.json", "r")
        table_schema_obj = json.load(table_schema_file)
        
        table_indices_file = open(self.path + "\\" + "indices.json","r+")
        table_indices_obj = json.load(table_indices_file)
        exist = False
        for schema_indix in table_schema_obj["indices"]:
            for index in table_indices_obj["indices"]:
                if index["name"] == schema_indix:
                    key = self.json_obj[schema_indix]
                    for dict in index["values"]:
                        if dict["key"] == key:
                            if(str(self.json_obj["id"])not in dict["value"]):
                                dict["value"].append(str(self.json_obj["id"]))
                            exist = True
                    if not exist:
                        new_dict = {
                            "key" : key,
                            "value" : [str(self.json_obj["id"])]
                        }
                        index["values"].append(new_dict)
        # print(table_indices_obj)
        # print(type(table_indices_obj))
        table_indices_file.close()
        table_schema_file.close()
        with open(self.path + "\\" + "indices.json","w") as table_indices_file:
            json.dump(table_indices_obj,table_indices_file, indent = 2)
        #table_indices_file.write(json_data)

        


    def execute(self):
        self.mk_new_file()
        self.update_indices()
        pass




'''
python main.py -cmd set -db csed2025 -tb Students -val
'''
'''
"'{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}'"
'''