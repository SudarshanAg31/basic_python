#Instance attributes=which is different for all object i.e=name,marks,etc

#class attributes=which is same for all the object i.e=collage_name,human,etc
class student:
    collage="G.L.A universty"
    def __init__(self,name,age):
        self.x=name
        self.z=age
s1=student("sudarshan",19)
print(s1.x)
print(s1.z)
print(student.collage)
#--------or---------
print(s1.collage)

#NOTE: i take x & z for better understanding 
#that .x and .z is use to store value of object form class