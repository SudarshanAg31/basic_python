#polymorphism:(operator overloading)
#when the same operator is allowed to have different meaning
#according to the context.
#meaning of operator overloading
# i.e print(1+2)# result 3
#print("sudarshan"+"agrawal")#it concatenate
#print([1,2,3]+[4,5,6])#merge
#NOTE:here the meaning of + is different for all this is known as operator overloading
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return complex(newReal,newImg)
num1=complex(1,2)
num1.shownumber()
num2=complex(2,3)
num2.shownumber()
num3=num1+num2
num3.shownumber()
num3=num1-num2
num3.shownumber()