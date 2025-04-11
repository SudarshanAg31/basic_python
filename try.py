n=int(input())
s=[]
for i in range(0,n):
    x=input()
    s.append(x) 
s=set(s)
s=len(s)
print(s)