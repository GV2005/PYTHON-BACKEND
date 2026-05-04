class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

student1=student("giri",21,"backend")
student2=student("mark",23,"mern")

print(student1.name,student1.age,student1.course)
print(student2.name,student2.age,student2.course)