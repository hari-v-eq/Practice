
class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @classmethod

    def from_price(cls,name,price):
        return cls(name, (price*80))

    def show(self):
        print(self.name, self.price)

class Car(Vehicle):
    def average(self,distance, fuel_used):
        milage=distance/fuel_used
        print(self.name, 'Milage',milage)
 

bmw_us=Car("BMW_200", 65000)
bmw_us.show()


bmw_ind=Car.from_price("BMW_200", 65000)
bmw_ind.show()


print(type(bmw_us))