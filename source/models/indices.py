from abc import ABC, abstractmethod
import os
from outputs.exceptions import FileNotFound
from models.table import Table

class index(ABC):
    def __init__(self, DB_name, table_name):
        self.indices_path = DB_name + "\\" + table_name + "\\indices" 
        self.DB_name = DB_name
        self.table_name = table_name

    def getIndicesNames(self):
        return os.listdir(self.indices_path)

    def getPKs(self, indexName, index):
        file_path = self.indices_path + "\\" + indexName + "\\" + index + ".txt"
        if not os.path.isfile(file_path):
            raise FileNotFound(message = "this index has not been saved to the database yet")
        with open(file_path,"r")as pks:
            PKs = pks.read().split(",")
        return PKs
    
    def addIndices(self, row_obj):
        table = Table(self.DB_name, self.table_name)
        for indexName in self.getIndicesNames():
            indices_path = self.indices_path + "\\" + indexName + "\\" + row_obj[indexName] + ".txt"
            old_pks = set()
            if os.path.isfile(indices_path):
                old_pks = set(self.getPKs(indexName, row_obj[indexName]))                
            old_pks.add(row_obj[table.getPrimaryKey()])
            with open(indices_path, mode ="w") as file:
                file.write(",".join(old_pks))

    def deleteIndices(self, row_obj):
        table = Table(self.DB_name, self.table_name)
        for indexName in self.getIndicesNames():
            index_path = self.indices_path + "\\" + indexName + "\\" + row_obj[indexName] + ".txt"
            is_empty = False
            with open (index_path, "r")as index_file:
                data = index_file.read().split(",")
                data.remove(row_obj[table.getPrimaryKey()])
                if len(data)>0:
                    new_data = ",".join(data)
                    with open (index_path , "w")as index_file:
                        index_file.write(new_data)
                else :
                    is_empty = True
            if is_empty:
                os.remove(index_path)