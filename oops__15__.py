#class method: A class is bound to the class & 
# receives the class as an implicit first argument.
#NOTE:static method can't access or modify class state & generally for utility
class person:
    name="no name"
    def __init__(self,name):
        self.name=name
        
p1=person("sudarshan")
print(person.name)
#so we can't change name to class name "sudarshan" 
#there are three methods:-
#first method
class person:
    name="no name"
    def __init__(self,name):
        person.name=name
        
p1=person("sudarshan")
print(person.name)
#second method
class person:
    name="no name"
    def __init__(self,name):
        self.__class__.name=name       
p1=person("sudarshan")
print(person.name)
#third method
class person:
    name="no name"
    @classmethod
    def __init__(cls,name):
        cls.name=name      
p1=person("sudarshan")
print(person.name)
#NOTE:@staticmethods()#no argument is pass
#@classmethods(cls)#first argument as cls
#instancemethods(self)#first argument as self    
