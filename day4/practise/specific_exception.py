try:
    a=int(input("Enter number :"))
    print(100/a)

except ValueError:
    print("numbers only")

except ZeroDivisionError:
    print("cannot / by 0")