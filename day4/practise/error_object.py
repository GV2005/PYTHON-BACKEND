try:
    a=int(input("Enter num :"))
    print(100/a)

except ValueError as e:
    print("value error :",e)

except ZeroDivisionError as e:
    print("Math error :",e)
