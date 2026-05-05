try:
    age=int(input("Enter Age :"))

    if age < 0 or age >=120:
        raise ValueError("age cannot be negative or more than 120yrs")
    
    print("valid Age")

except ValueError as e:
    print("error :",e)