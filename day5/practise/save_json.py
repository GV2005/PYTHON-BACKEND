import json

user={
    "name":"giri",
    "age":21,
    "goal":"Python developer"

}


with open("profile.json","w") as file:
    json.dump(user,file)