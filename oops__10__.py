#private:it is use to private our information.we use this for make our method and attributes(__)
class account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num=acc_num
        self.__acc_pass=acc_pass
    def __reset(self):
        print(self.__acc_pass)
    def hack(self):
        self.__reset()
        
acc1=account("1234",544)
print(acc1.acc_num)
'''print(acc1.acc_pass)'''
"""acc1.__reset()"""
#NOTE:so we make acc__pass & reset() as private so we can't access as an object
#but in same class we can access it and call to another function 
#if we call private (method or attribute) to another function and call  this function 
#which is not private so it return our private information. 
acc1.hack()

         