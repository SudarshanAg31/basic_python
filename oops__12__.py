#Multi-level Inheritance
class cars:
    @staticmethod
    def car_start():
        print("car is start...")
    @staticmethod
    def car_stop():
        print("car is stop...")
class brand(cars):
    def __init__(self,name_brand):
        self.name_brand=name_brand
class Fortuner(brand):
    def __init__(self, type):
        self.type=type
car=Fortuner("petrol")

print(car.type)
car.car_start()       
#NOTE:-we call car_start() from cars class 
