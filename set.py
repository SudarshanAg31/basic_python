#set={} unordered and immutable,add or remove is ok.No duplicates

string={"apple","banana","orange","coconat"}
num={1,2,3,4,5,6,7,8}
#print(len(string))#for length of string
#print("pineapple" in string)# it return true and false:- (answer is false)

#note:- we can not add any string ussing index method because of unordered beheaver

#string.add("pineapple")# we can add string in unordered way
#string.remove("apple")# we can remove string in unordered way
#string.pop()#it remdomly remove first string form sets
#string.clear()#it remove all string form sets
#string.discard()#remove an element if it exists,but does not raise if the element is not found> 

#x=string|num #|it add two set (|) union
#x=string&num #it return common code(&)intersection
#x=string-num #it return element in first but not in second(-)
#x=string^num #it return not common element in but  the set(^)

print(x)
for x in string:
    print(x)