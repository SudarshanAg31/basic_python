#Instance attributes=which is different for all object i.e=name,marks,etc

#class attributes=which is same for all the object i.e=collage_name,human,etc
class student:
    collage="G.L.A universty"
    num_student=0
    def __init__(self,name,age):
        self.x=name
        self.z=age
        student.num_student+=1
s1=student("sudarshan",19)
s2=student("love",17)
print(s1.x)
print(s1.z)
print(student.collage)
#--------or---------
#print(s1.collage)
print(student.num_student)

#NOTE: i take x & z for better understanding 
#that .x and .z is use to store value of object form class