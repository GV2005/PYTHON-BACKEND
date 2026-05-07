from app.models.user import Users
from app.validators.user_validator import validate_email,validate_age


def create_user(name: str, age: int, email: str):
    validate_age(age)
    validate_email(email)

    user = Users(name, age, email)

    return user