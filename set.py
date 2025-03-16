#set={} unordered and immutable,add or remove is ok.No duplicates

string={"apple","banana","orange","coconat"}
#print(len(string))#for length of string
#print("pineapple" in string)# it return true and false:- (answer is false)

#note:- we can not add any string ussing index method because of unordered beheaver

#string.add("pineapple")# we can add string in unordered way
#string.remove("apple")# we can remove string in unordered way
#string.pop()#it remdomly remove first string form sets
#string.clear()#it remove all string form sets
for x in string:
    print(x)