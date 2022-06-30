sample_data = [
    {"userId": 1,  "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1,  "name": "ram", "completed": False},
    {"userId": 1,  "name": "ravan", "completed": True}
]

#python walrus operator example
for row in sample_data:
  if name:= row.get("name"):
    print(f"{name} found")
  else:
    pass

#above code without walrus operator example
for row in sample_data:
  name = row.get("name")
  if name:
    print(f"{name} is present")
  else:
    pass
    