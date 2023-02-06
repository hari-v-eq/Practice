class Student:
    school_name="ABC"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def change_school(cls,name):
        print(Student.school_name)
        Student.school_name=name

name_1=Student("Hariom",26)

print(Student.change_school('XYZ School'))
print(Student.school_name)
