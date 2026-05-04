class person:
    def __init__(self,name):
        self.name=name
    
    def introduce(self):
        return (f"i am {self.name}")
    
class developer(person):

    def code(self):
        return (f"{self.name} can code")
    
dev1=developer("giri")

print(dev1.introduce())
print(dev1.code())
        