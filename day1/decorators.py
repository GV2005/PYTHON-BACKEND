
def car_price(value):
    def wrapper():
        print("NO BARGAIN")
        value()
        print("FIXED PRICE")
    return wrapper

def value():
    print("5000000rs")

showroom=car_price(value)
showroom()