
class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
c1=circle(4)
print(c1.radius)
print(c1.area())    
print(c1.perimeter())

class employe:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showdetail(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
e1=employe("accountant","finance","50K")
e1.showdetail()        