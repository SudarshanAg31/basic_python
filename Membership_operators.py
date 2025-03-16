#Membership operator = used to test whether a value or varible is found in a sequence
#                      (string,list,tuple,set ,or dictionary)
#                       1. in 
#                       2. not in  
#string:
name="sudarshan agrawal"
if "a" in name and "s" in name:
    print("yes")
else:
    print("no")
    
#list:
number=[2,3,4,5,6,7,8,9,10]
if 1 not in number and 2 in number:
    print("yes")
else:
    print("no")
    
#tuple:
number=(2,3,4,5,6,7,8,9,10)
if 1 not in number and 2 in number:
    print("yes")
else:
    print("no")
    
#set:
number={2,3,4,5,6,7,8,9,10}
if 1 not in number and 2 in number:
    print("yes")
else:
    print("no")
    
#dictionary:
my_dictionary={"sudarshan":"O",
               "tanvi":"A+",
               "dhruv":"A",
               "love":"F"}
if "sudarshan" in my_dictionary:
    print("yes")
else:
    print("no")

if "O" in my_dictionary.values():
    print("yes")
else:
    print("no")