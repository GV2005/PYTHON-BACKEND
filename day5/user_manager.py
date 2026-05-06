import json
import os

class UserManager:

    def add_user(self,name,age,role):
        if not os.path.exists("database.json"):
                with open("database.json","w") as file:
                    json.dump([],file)
        
        with open("database.json","r") as file:
            data=json.load(file)

        new_user={
            "name":name,
            "age":age,
            "role":role
        }

        data.append(new_user)

        with open("database.json","w") as file:
            json.dump(data,file)
    
    def view_user(self):
        try:
            with open("database.json","r") as file:
                data=json.load(file)
                for users in data:
                    print(users)
        except FileNotFoundError as e:
            print("no database")
    
    def find_user(self,name):
        try:
            with open("database.json","r") as file:
                data=json.load(file)

                for users in data:
                    if users["name"]==name:
                        print(users)
                return
            print("user not found")
        except FileNotFoundError:
            print(f"no user named {name} exist")