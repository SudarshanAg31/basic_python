data=[]
for i in range(1,6):
    value=int(input("enter number:"))
    data.append(value)
data.sort()
for i in data:
    print(i,end=" ")