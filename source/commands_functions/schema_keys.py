from abc import ABC

class Keys(ABC):
    SCHEMA = "schema"
    DATABASE_NAME = "database_name"
    TABLES  = "Tables"
    NAME = "name"
    COLUMNS = "columns"
    PRIMARY_KEY = "primary_key"
    INDEX_KEY = "Index_keys"
    CONSISTENTLY = "consistently"
    ENABLE_OVERWRITE = "enable_overwrite"