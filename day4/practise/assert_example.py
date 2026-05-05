age=int(input("enter age :"))
password=input("enter password :")

assert age>0,"age can't be negative"
print("valid age")

assert len(password)>=8,"weak password"
print("valid password")