#normaly it take input in the form of string so (age=age+1) not work properly so we 
# convert input as int so now its work properly (age=age+1)
name=input("enter your name ")
age=int(input("enter your age "))
age=age+1
print(f"your is {name}")
print(f"your age is {age}")