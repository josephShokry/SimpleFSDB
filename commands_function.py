import os
from abc import ABCMeta,abstractclassmethod, abstractstaticmethod
import json

class Icommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def excute():
        """the interface Icommand"""

class commandfactory:
    @staticmethod
    def build_command(args):
        command_type=args.command
        if command_type == "create":
            return create()
        elif command_type == "delete":
            return delete()
        elif command_type == "get":
            return get()
        elif command_type == "set":
            return set()

class create(Icommand):
    def excute(self,args):
        f=open(args.schema,"r")
        schima=json.load(f)
        parent_dir=os.getcwd() #get the current dir of the project
        data_base_name=schima["database_name"]
        path=os.path.join(parent_dir,data_base_name)
        if not os.path.isdir(path): #to check if the DB directory is created before or not
            os.mkdir(path)
        for i in schima["Tables"]:
            table_path=os.path.join(path,i["name"])
            if not os.path.isdir(table_path):
                os.mkdir(table_path)
                # file_name=os.path.join(table_path,"info.txt")
                # f=open(file_name,'w')
                # f.write(json.dumps(i, indent = 4))

    

def delete(primary_key):
    print("dummy will be implemented later")

def get(primary_key):
    print("dummy will be implemented later")

def set(primary_key,value):
    print("dummy will be implemented later")