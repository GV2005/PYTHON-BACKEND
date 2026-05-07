skills:list[str]=["python","sql","fastapi"]
marks:list[int]=[45,56,67,78]
profile:dict[str,str]={
    "name":"giri",
    "job":"developer"
}

def get_languages() -> list[str]:
    return ["tamil","english","russian"]

print(skills)
print(marks)
print(profile)
print(get_languages())