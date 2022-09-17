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
    def __init__(self, database_name, table_name, value, disableoverwrite, value_path):
        self.table = Table(database_name, table_name)
        if disableoverwrite == "true" :
            self.disableoverwrite = True
        else :
            self.disableoverwrite = False 
        self.indices = index(DB_name = database_name, table_name = table_name)
        self.json_obj = self.table.load_value(value = value,value_path = value_path)

    def execute(self):
        new_row = dict()
        for column in self.table.getColumns():
            new_row[column] = self.json_obj[column]
        if not self.disableoverwrite and os.path.isfile(self.table.table_path + "\\" + new_row[self.table.getPrimaryKey()] + ".json"):
            with open(self.table.table_path + "\\" + new_row[self.table.getPrimaryKey()] + ".json", 'r') as old_row: 
                old_obj = json.load(old_row)
            self.indices.deleteIndices(old_obj)
        self.table.writeNewRow(new_row, self.disableoverwrite)
        self.indices.addIndices(new_row)