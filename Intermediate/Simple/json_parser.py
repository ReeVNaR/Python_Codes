import json

data = '{"name": "Alice", "age": 25, "city": "New York"}'
parsed_data = json.loads(data)

print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
