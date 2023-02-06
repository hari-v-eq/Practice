class Employee:
    company_name="ABC"

    def __init__(self,name,address):
        self.name=name
        self.address=address

    @classmethod

    def change_name(cls,company_name):
        cls.company_name=company_name

    def display(self):
        print(self.name, self.address, Employee.company_name)

hari=Employee("Hariom","Ahmedabad")

hari.display()


Employee.change_name("XYZ")

hari.display()