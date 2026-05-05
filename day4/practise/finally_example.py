try:
    a=int(input("Enter number :"))
    res=(100/a)

except ValueError:
    print("numbers only")

except ZeroDivisionError:
    print("cannot / by 0")

else:
    print("Calculation Successful :",res)

finally:
    print("Execution Completed")