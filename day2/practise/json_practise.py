import json

user={
    "name":"giri",
    "age":21,
    "goal":"backend developer"
}

profile=json.dumps(user)

print(profile)
print(type(profile))


user=json.loads(profile)

print(user)
print(type(user))