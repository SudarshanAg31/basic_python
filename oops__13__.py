#Multiple Inheritance
class start:
    def starts(self):
        print("car start...")
class stop:
    def stops(self):
        print("car stop...")
class car(start,stop):
    def __init__(self):
        print("car")
c1=car()
c1.starts()
c1.stops()
    