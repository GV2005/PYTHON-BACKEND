try:
    with open("missing.txt","r") as file:
        data=file.read()

    print(data)

except FileNotFoundError as e:
    print("sorry, file not found")