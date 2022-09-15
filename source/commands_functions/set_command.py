import os, json
from commands_functions.abstract_command import AbtractCommand
from outputs.exceptions import *
from models.table import *
from models.indices import index;
'''
- json file objecte will created in the validate its name is the pk and pares it here to an object file 
- then the execute will take the parsed file object and the parsed json value and will write the values of the (value)
in the file 
- then will update the indices
''' 
class SetCommand(AbtractCommand):
    def __init__(self, data_base_name, table_name, value, disableoverwrite, value_path):
        self.table = table_set(data_base_name, table_name)
        self.disableoverwrite = disableoverwrite
        # self.table.validate(disableoverwrite)
        #  self.validate(data_base_name, table_name, value, disableoverwrite, value_path)
        self.table.loadTableSchema(DB_name = data_base_name, table_name = table_name)
        self.indices = index(DB_name = data_base_name, table_name = table_name)
        self.json_obj = self.table.load_value(value = value,value_path = value_path)

    def execute(self):
        new_row = dict()
        for column in self.table.getColumns():
            new_row[column] = self.json_obj[column]
        self.table.writeNewRow(new_row,self.disableoverwrite)
        self.indices.addIndices(new_row)
        
        




'''
python main.py -cmd set -db csed2025 -tb Students -val
'''
'''
"{\"id\": \"5\",\"first_name\": \"joseph\",\"last_name\": \"shokry\",\"age\": \"20\",\"gender\": \"male\"}"
'''