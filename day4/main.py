from user import USER
try:
    user1=USER("giri",21,"test4@gmail.com","testing4&8")
    print(user1.introduce())

except Exception as e:
    print("Regesteration Failed :" , e)