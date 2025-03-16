#indexing:accessing elements of a sequence using [] (indexing operator)
#           [start: end: step]
credit_number="1234-5278-5433-6735-5677"
print(credit_number[0])#start index
print(credit_number[:4])#it start form 0 index and end on 4 index
print(credit_number[0:8])#it start form 0 index and end on 8 index
print(credit_number[4:])#it start form 4 index and end on last index
print(credit_number[::3])#it start form 0 index and end on last index and it moves with 3
print(credit_number[-1])# it start form end
print(credit_number[-4:])# it print last for digit

#                  important
print(credit_number[::-1])#it reverse string