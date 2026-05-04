class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def introduce(self):
        return (f"i am {self.name}")

    def study(self):
        return (f"{self.name} is studying {self.course}")

student1=student("giri",21,"backend")
student2=student("prataph",20,"java")

print(student1.introduce())
print(student2.study())