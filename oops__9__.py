#del keyword: used to delete object properties or object itself.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("Sudarshan Agrawal",19)
del s1.age
print(s1.name)
del s1
print(s1.age,s1.name)
#NOTE: if we use (del s1) so it delete whole s1 (object)
#NOTE: if we use(del s1.name) so it delete name in s1 (object properties) 