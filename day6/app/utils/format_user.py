from app.models.user import Users

def format_user(user: Users) -> str:
    return (
        f"User Details\n"
        f"------------\n"
        f"Name  : {user.name}\n"
        f"Age   : {user.age}\n"
        f"Email : {user.email}"
    )
