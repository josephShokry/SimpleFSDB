from abc import ABC
from imp import PKG_DIRECTORY
from msilib import schema
from tkinter.tix import COLUMN

class SchemaKeys():
    SCHEMA = "schema"
    DB_NAME = "database_name"
    TABLES  = "Tables"
    NAME = "name"
    COLUMNS = "columns"
    PK = "primary_key"
    INDEX_KEY = "Index_SchemaKeys"
    CONSISTENTLY = "Consistently"