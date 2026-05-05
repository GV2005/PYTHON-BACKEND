def validate_age(age):
    if age <0:
        raise ValueError("age can't be negative")
    if age>120:
        raise ValueError("age is abnormal")
    

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")
    

def validate_password(password):
    if len(password) < 8:
        raise ValueError("weak password")
    

try:
    validate_age(-25)
    validate_email("123gmail.com")
    validate_password("uh5678")
    print("Valid Format")

except ValueError as e:
    print("Error :",e)