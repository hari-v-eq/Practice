
class Base:
    def __init__(self,name):
        self.name=name
    def display(self):
        return self.name

class Child(Base):
    def __init__(self, name,age):
        self.age=age
        Base.__init__(self,name)

    def getage(self):
        return self.age

class Grandchild(Child):
    def __init__(self, name, age, address):
        self.adderess=address
        Child.__init__(self,name,age)
    def getaddress(self):
        return self.adderess        
        

g=Grandchild("Niva",34, "America")

print(g.getaddress(),g.getage(),g.display())
