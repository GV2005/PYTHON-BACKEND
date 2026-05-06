with open("notes.txt","r") as file:
    content=file.read()
    print(content)

with open("updated.txt","w") as file2:
    file2.write("created to practise with open\n")
    file2.write("second line for demo\n")

with open("updated.txt","r") as file2:
    for line in file2:
        print(line.strip())