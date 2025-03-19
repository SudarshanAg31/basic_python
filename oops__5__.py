#practice question
#create student class that take name & marks of 3 subject as arguments
#in constructor.
#then create a method to print the average.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avrage(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"here is your avrage score",sum/3)
        
s1=student("sudarshan",[77,88,99])
s1.avrage()

        
        