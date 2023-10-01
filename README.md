# SimpleFSDB
The Simple File System Database is a lightweight, command-line-based database system designed for simple data storage and retrieval.  
This README provides an overview of the project structure, how to use it, and key components of the system.

## Getting Started

To get started with the Simple File System Database, follow these steps:

### Prerequisites

1. Python 3.x installed on your machine.

### Installation

1. Clone or download the project to your local machine.

### Usage
To use this database you need to pass the commands by CMD so we made SimpleDBDriver in Java you can use it to call the database 
1. Navigate to the project directory.
2. Run the main script to execute database commands:

   ```python
   python main.py -cmd [command] [options]
   ```

   Replace `[command]` with the desired database command and `[options]` with relevant command options.

   Example usage:

   - Creating a new database:
     ```python
     python main.py -cmd create -sch schema.json
     ```

   - Setting a new value in the database:
     ```python
     python main.py -cmd set -database my_database -table my_table -val '{"key": "value"}'
     ```

   - Querying data from the database:
     ```python
     python main.py -cmd query -database my_database -table my_table -q '{"key": "value"}'
     ```


## DB Available Commands
| Name | parameters | Description |
|------|------------|-------------|
| `create` | DatabaseSchemaPath | Create database which follow input [schema](#schema-sample) |
| `set` | DatabaseName, TableName, Inputdata | Set row with the input data |
| `get` | DatabaseName, TableName, InputQuery | Use the query to get specific data |
| `delete` |  DatabaseName, TableName, InputQuery | Use the query to delete specific data |
| `clear`|  DatabaseName | return the database to the initial state |

## sample Schema:
```json
{
  "database_name": "ClassA1",
  "Tables": [
    {
      "name": "student",
      "columns": [
        "First_name",
        "Last_name",
        "CGPA",
        "Gender",
        "Age"
      ],
      "primary_key": "Last_name",
      "index_keys": [
        "First_name",
        "Last_name",
        "CGPA"
      ],
      "overwrite": "True",
      "consistently": "Eventual"
    }
  ]
}
```
## Table Contents:


  | Name | Type | Nullable | Notes |
  | ---- | ---- | -------- | ----- |
  | Name | string | No | |
  | Columns | List of Strings | No | should contain the primary-key |
  | Primary_key | String | No | |
  | Index_key | List of Strings | No | |
  | Overwrite | String | No | should be True or False only |
  | Consistently | String | No | |


---
