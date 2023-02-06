# class Person:
#     def __init__(self,name,mobile):
#         self.name=name
#         self.mobile=mobile
#     def person_info(self,name,mobile):
#         print("Inside person_info....")
#         print(self.name, self.mobile)

# class Company:
#     def company_info(self,company_name,address):
#         self.company_name=company_name
#         self.address=address
#     def show(self):
#         print("Inside company_info.....")
#         print(self.company_info, self.address)
# class Employee(Person,Company):
#     def employee_info(self,salary,skill):
#         self.salary=salary
#         self.skill=skill
#         
#     def show2(self):
#         print("inside employee_info.....")
#         print(self.salary, self.skill)


# emp = Employee()

# emp.person_info("Hari", 8866249010)
# emp.company_info("XYZ company", "Ahmedabad")
# emp.employee_info(20000, "Python developer")


# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
