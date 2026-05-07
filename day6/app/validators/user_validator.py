def validate_age(age:int) -> bool:
    if age<0:
        raise ValueError("age cant be negative")
    elif age>120:
        raise ValueError("age is abnormal")


def validate_email(email:str):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")
    