import json
jsonData='{"fname": "joseph","lname": "shokry","age": 32}'
print(jsonData)
data=json.loads(jsonData)
print(type(data))
print(data["fname"])