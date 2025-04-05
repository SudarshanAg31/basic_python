add=lambda x,y:x+y
print(add(100,200)) 
# for one line function we use lambda
# filter(function,collection)= return all value that pass a condition
filr=[10,20,30,40,50,60,70,80,90,100]
fil_r=list(filter(lambda filr:filr>30,filr))
print(fil_r)