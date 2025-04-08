#ENUMERATE:-it allows us to get the index value of each element
#in the sequence at same time
marks=[77,88,66,99,74,86,45,96]
for index,marks in enumerate(marks):
    print(marks)
    if index==3:
        print("good")
#at same time it give index value