from abc import ABC

class Keys(ABC):
    SCHEMA = "schema"
    database_name = "database_name"
    TABLES  = "Tables"
    NAME = "name"
    COLUMNS = "columns"
    primary_key = "primary_key"
    INDEX_KEY = "Index_keys"
    CONSISTENTLY = "Consistently"