#Iterables:- An object/ collection that can return its elements one at a time,
# allowing it to be iterated over in a loop
number=[1,2,3,4,5,6,7,8,9,10]
for i in number:
    print(i)
#NOTE= its same for tuple,set(not in a case of reverse)
name="sudarshan agrawal"
for i in name:
    print(i,end="")
print()
#its for string
my_dictionary={"A":1,"B":2,"C":3}
for i,j in my_dictionary.items():
    print(f"{i}:{j}")
#its for dictionay