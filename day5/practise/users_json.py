import json
users=[
    {"name":"giri","age":21},
    {"name":"hari","age":22},
    {"name":"arun","age":23}
]

with open("userProfile.json","w") as file:
    json.dump(users,file)

with open("userProfile.json","r") as file:
    data=json.load(file)

print(data)
print(data[0]["name"])
print(data[1]["age"])
print(data[2]["name"])