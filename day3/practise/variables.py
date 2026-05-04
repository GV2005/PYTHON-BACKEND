class Employee:
    company="GV fintech"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=Employee("Giri",45000)
emp2=Employee("Hari",75000)

print(f"{emp1.name} is working in {emp1.company} for salary {emp1.salary}")
print(f"{emp2.name} is working in {emp2.company} for salary {emp2.salary}")
