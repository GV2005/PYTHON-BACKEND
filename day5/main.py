from user_manager import UserManager

user1=UserManager()
user2=UserManager()

user1.add_user("giri",21,"developer")
user2.add_user("hari",23,"designer")

user1.view_user()

user1.find_user("hari")
