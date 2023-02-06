class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("My name is : " +self.name)

p1=Person("Hariom", 26)

p1.myfun()