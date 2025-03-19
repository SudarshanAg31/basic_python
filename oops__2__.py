 #__init__Function
 #constructor
 #All class have a function called __init__(),
 #which is always executed when the object is being initiated.
 #python create constructor for usser 
 # and we always pass self argument to constructor
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database...")

s1=student("sudarshan",98)
print(s1.name)
print(s1.marks)

s2=student("love",99)
print(s2.name)
print(s2.marks)
#here we pass sudarshan to name in def__init__

#s1 is same as self

#we created self.name where .name is a varible of object and
#the name we pass to self.name is sudarshan

#at last we print s1.name to print sudarshan