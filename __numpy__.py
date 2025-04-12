#this is the basic structure of array using numpy
#(np.int8):is use for given size of data
import numpy as np
myarr=np.array([3,6,7,8,9],np.int8)
print(myarr)
print(myarr.shape)
print(myarr.size)
print(myarr.dtype)
myarr[0]=45
print(myarr)
print()
print()
print()
#it create zeros arr 
x=np.zeros((2,5))
print(x)
#it create arr for given (n-1) range
y=np.arange(15)
print(y)  
#it is use to equal space (start,end,space)
z=np.linspace(1,50,10)
print(z)
#it is use to create empty arr with random values
a=np.empty((4,6))
print(a)
#it create an identity mtrx 
i=np.identity(45)
print(i)