class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=(self.phy+self.chem+self.math)/3
s1=student(93,90,70)
print(f"{s1.percentage:.2f}%")
s1.math=80
print(f"{s1.percentage:.2f}%")
#if i want to update my maths marks so it can't change
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return(self.phy+self.chem+self.math)/3
s1=student(93,90,70)
s1.math=80
print(f"{s1.percentage:.2f}%")
#property()change its value when we update it..... 
    
        