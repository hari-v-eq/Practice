class Student:
    school_name="Dayamayi"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    

    @classmethod
    
    def change_school(cls,school_name):
        cls.school_name=school_name
    def show(self):
        print(self.name, self.age, " School is : ", Student.school_name)


hari=Student("Hari",26)

hari.show()

Student.change_school("DSP")
hari.show()