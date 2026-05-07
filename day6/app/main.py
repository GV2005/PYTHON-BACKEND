from app.services.user_services import create_user
from app.utils.format_user import format_user


user = create_user("Giri", 21, "giri@gmail.com")

print(format_user(user))