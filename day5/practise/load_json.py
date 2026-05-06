import json

with open("profile.json","r") as file:
    data=json.load(file)

print(data)
print(type(data))
print(data["age"])