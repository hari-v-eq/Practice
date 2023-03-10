# use of class method and static method

from datetime import date


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        #class method for birthdate
    @classmethod    
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
        #static Method
    @staticmethod
    def adult(age):
        return age>18

person1=Person("Mayank",21)
person2 = Person.fromBirthYear('Mayank',1996)

print(person1.age)
print(person2.age)

print(Person.adult(19))
