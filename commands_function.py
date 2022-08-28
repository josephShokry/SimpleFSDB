import os
def create(schima):
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