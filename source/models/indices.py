from abc import ABC, abstractmethod
import json, os
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
        table = Table()
        table.loadTableSchema(self.DB_name, self.table_name)
        for indexName in self.getIndicesNames():
            file_path = self.indices_path + "\\" + indexName + "\\" + row_obj[indexName] + ".txt"
            index_file_data = ""
            if os.path.isfile(file_path):
                with open(file_path,"r")as old_data:
                    index_file_data = old_data.read()
            with open(file_path,"w")as index_file:
                if index_file_data != "":
                    index_file.write(index_file_data + "," + row_obj[table.getPrimaryKey()])
                else : index_file.write(row_obj[table.getPrimaryKey()])

    def deleteIndices(self, row_obj):
        table = Table()
        table.loadTableSchema(self.DB_name, self.table_name)
        for indexName in self.getIndicesNames():
            index_path = self.indices_path + "\\" + indexName + "\\" + row_obj[indexName] + ".txt"
            with open (index_path, "r")as index_file:
                data = index_file.read().split(",")
                data.remove(row_obj[table.getPrimaryKey()])
                new_data = ",".join(data)
            with open (index_path , "w")as index_file:
                index_file.write(new_data)