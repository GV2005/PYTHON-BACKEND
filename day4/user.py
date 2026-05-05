from validators import *

class USER:
    def __init__(self,name,age,email,password):
        validate_age(age)
        validate_email(email)
        validate_password(password)

        self.name=name
        self.age=age
        self.email=email
        self.password=password


    def introduce(self):
        print(f"Hi! I am {self.name} , aged {self.age} here is  my email {self.email} and password is{self.password}")

    