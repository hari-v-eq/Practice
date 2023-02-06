class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self,name,age,year):
        Person.__init__(self,name,age)
        self.graduationyear=year
    def greetings(self):
        print("Welcome",self.name , "to the class of" , self.graduationyear)

x=Student("Hariom",27, 2020)

x.display()
x.greetings()
print(x.graduationyear)