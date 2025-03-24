#super()=super()method is used to access methods of the parent class.
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car start...")
    @staticmethod
    def stop():
        print("car stop...")
class toyotacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
c1=toyotacar("fortuner","petrol")
c1.stop()
print(c1.name)
print(c1.type)
c1.stop()
#NOTE:-by super() function we call type which is in different class 
# and it is the part od __init__() function...
#if we not use super() function it show error 