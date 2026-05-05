class InvalidAgeError(Exception):
    pass

try:
    age=int(input("Enter age :"))

    if age<0:
        raise InvalidAgeError("age cannot be negative")

    elif age>=120:
        raise InvalidAgeError("age is out of range")

    print("valid age")

except InvalidAgeError as e:
    print("Error :",e) 

