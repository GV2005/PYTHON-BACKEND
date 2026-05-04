class Employee:
    def work(self):
        return ("employee is working")
    
class developer(Employee):
    def work(self):
        return ("developer developes system")
    
class designer(Employee):
    def work(self):
        return ("designer design UI")
    

dev1=developer()
des1=designer()

print(dev1.work())
print(des1.work())
