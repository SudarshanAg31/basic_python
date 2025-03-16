"""result=input("enter your name:")
while result=="":
    result=input("enter your name:")    
print(f"your name {result}")
"""
result=int(input("enter number is b/w (0-10): "))
while result<0 or result>10:
    result=int(input("enter number: "))
print(f"your number: {result}")