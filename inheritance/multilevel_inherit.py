#multilevel

class Vehicle:
    def vehicle_info(self):
        print("in vehicle info")

class Car(Vehicle):
    def car_info(self):
        print("In car info")

class sportscar(Car):
    def sportscar_info(self):
        print("In sportscar")



car=sportscar()

car.car_info()
car.vehicle_info()
car.sportscar_info()