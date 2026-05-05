from exception import *

def validate_age(age):
    if age<0:
        raise InvalidAgeError("age can't be negative")
    if age>=120:
        raise InvalidAgeError("age is abnormal")
    
def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email address")
    
def validate_password(password):
    if len(password)<8:
        raise WeakPasswordError("password is too weak")
    
    