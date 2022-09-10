from abc import ABC

class Keys(ABC):
    SCHEMA = "schema"
    DB_NAME = "database_name"
    TABLES  = "Tables"
    NAME = "name"
    COLUMNS = "columns"
    PK = "primary_key"
    INDEX_KEY = "Index_keys"
    CONSISTENTLY = "Consistently"