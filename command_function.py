import os
from abc import ABCMeta,  abstractstaticmethod
import json
from Schema_keys import Schema_keys


class Icommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def excute():
        """the interface Icommand"""

class commandfactory:
    @staticmethod
    def build_command(args):
        command_type=args.command
        if command_type == "create":
            return create(args.schema_file)
        elif command_type == "delete":
            return delete()
        elif command_type == "get":
            return get()
        elif command_type == "set":
            return set()
        
class create(Icommand):
    def __init__(self, schema_file):
        self.schema_file=schema_file
        schema = open(schema_file, "r")
        self.schema_data = json.load(schema)
        schema.close()

    def excute(self):
        schema_data=self.schema_data
        parent_dir = os.getcwd() #get the current dir of the project
        data_base_name = schema_data[Schema_keys.DB_NAME]
        path = os.path.join(parent_dir, data_base_name)
        if not os.path.isdir(path): #to check if the DB directory is created before or not
            os.mkdir(path)
        for table in schema_data[Schema_keys.TABLES]:
            table_path = os.path.join(path, table[Schema_keys.NAME])
            if not os.path.isdir(table_path):
                os.mkdir(table_path)
                # file_name=os.path.join(table_path, "info.txt")
                # f=open(file_name, 'w')
                # f.write(json.dumps(i,  indent = 4))

    
#this will be implemented later
class delete(Icommand):#add here the init function and initialize your paramater
     
    def excute(self):
        print("dummy delete will be implemented later")

class get(Icommand):
     
    def excute(self):
        print("dummy get will be implemented later")

class set(Icommand):
    def excute(self):
        print("dummy set will be implemented later")