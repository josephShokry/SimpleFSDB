import os
import json
def create(schima):
    parent_dir=os.getcwd()
    data_base_name=schima["database_name"]
    path=os.path.join(parent_dir,data_base_name)
    os.mkdir(path)
    for i in schima["Tables"]:
        table_path=os.path.join(path,i["name"])
        os.mkdir(table_path)
        file_name=os.path.join(table_path,"info.txt")
        f=open(file_name,'w')
        f.write(json.dumps(i, indent = 4))

def delete(primary_key):
    print("Hello from the delete function")

def get(primary_key):
    print("Hello from the get function")

def set(primary_key,value):
    print("Hello from the set function")