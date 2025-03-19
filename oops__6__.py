#static methods
#methods that don't use the self paremeter(work at class level)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def hello():
        print("hello")
    def intro(self):
        print("I am",self.name+" Agrawal","and i am",self.age,"years old.")
s1=student("Sudarshan",19)
s1.hello()
s1.intro()
#if we write s1.hello() it show error because there is no self 
#but we want to print hello for everyone so we use (@staticmethod)
#NOTE:now def hello() function is work as a class not an object
#NOTE:we use .self for object
 