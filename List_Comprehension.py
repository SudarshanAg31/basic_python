#list comprehension:A consise way to create lists in python
#                   compact and easier to read that traditional loops
#                   [expression for value in itreable if condition]

#common way 
list=[]
for i in range(1,11):
    list.append(i*2)
print(list)

#list comprehension
#example 1
list=[i*2 for i in range(1,11)]
print(list)
#example 2
square=[i*i for i in range(1,11)]
print(square)
#example 3
fruits=["apple","banana","coconut","orange"]
fruit_chars=[i.upper() for i in fruits]
print(fruit_chars)
#example 4
numbers=[1,-2,3,-4,5,-6]
list=[i*i for i in numbers if i>0]
list_ve=[i*i for i in numbers if i<0]
print(list)
print(list_ve)
#example 5
grade=[85,34,65,23,89,98,11,1,0,45,76]
result=[ i for i in grade if i>=33]
print(result)