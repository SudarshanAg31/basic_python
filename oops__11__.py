#Inheritance:-When one class(child/derived) derives the properties &
#methods of another class(parent/base).
#there are it is of 3 type Inheritance
#1)single Inheritance 2)Multi-level Inheritance 3)Multiple Inheritance 
#single Inheritance
class cars:
    @staticmethod
    def car_start():
        print("car is start")
    @staticmethod
    def car_stop():
        print("car is stop")
class toyota_car(cars):
    def __init__(self,name):
        self.name=name
car1=toyota_car("fortuner")
car2=toyota_car("prius")
car1.car_start()
print(car1.name)
print(car2.name)
car1.car_stop()


        