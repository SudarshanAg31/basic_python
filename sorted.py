#sorted():it is a built-in function used for sorting iterables
        # (list,tuple,dictionary,string etc).
        # it return value
        #convet into list
#NOTE: sort is a method of list class.
l=[3,4,5,67,3,4,56,7,54,34]
a=sorted(l)
print(a) 
s="sudarshan"
z=sorted(s)
print(z)
se_t={234,44,4,56,67,9,8,7,6,45,5,34,43}
s_se_t=sorted(se_t)
print(s_se_t)
#sorted() reverse=True:
k=sorted(se_t,reverse=True)
print(k)
#sorted() key=len:
q=["aaa","aa","a"]
q=sorted(q,key=len)
print(q)