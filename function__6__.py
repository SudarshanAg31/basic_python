#ARBITRARY
#*args     =allows you to pass muntiple non-key arguments 
#           *unpacking operator
#           1.positional ,2.defualt ,3.keyword,4.arbitrary
def add(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add(1,2,3,5,4,6,7,8,9))
# by ussing *args we can pass as much argument to our add function
# args is behave like list 
def add(*add):
    total=0
    for i in add:
        total+=i
    return total
print(add(1,2,3,5,4,6,7,8,9))
# we can change the args name with outher name ex: *add
