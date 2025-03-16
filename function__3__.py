#return use to return value form function 
def add (x,y):
    z=x+y
    return z
def sub (x,y):
    z=x-y
    return z

def mul (x,y):
    z=x*y
    return z

def div (x,y):
    z=x/y
    return z
    
a=10
b=12
print("EXAMPLE 1")
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
#    or

q=add(a,b)
print(q)
print()
#same for all

#example 2

def first_last(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last
print("EXAMPLE 2")
print(first_last("sudarshan","agrawal"))
#                   or
fullname=first_last("tanvi","agrawal")
print(fullname)