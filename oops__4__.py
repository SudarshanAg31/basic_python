#Methods: methods are functions that belong to objects.
class student:
    collage="G.L.A Universty"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def fullname(self):
        return self.name+" Agrawal"
    
    def age_(self):
        return self.age*self.age
s1=student("Sudarshan",19)
print(s1.name)
print(s1.age)
print(s1.age_())
print(s1.fullname())
print(student.collage)

#so fullname and age_ are the method use in this code