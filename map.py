#The map() function in Python is a built-in function 
# that applies a given function.
# to each item of an iterable (e.g., list, tuple, etc.) 
# and returns an iterator containing the results.

#map(function, iterable)

str_number=input()
#for input
int_number=str_number.split()
#we split string into different part and store in list
int_number=list(map(int,int_number))
#we convert string number into integer number
print(int_number)