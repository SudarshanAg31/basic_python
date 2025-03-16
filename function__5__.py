# keyword arguments: an argument preceded by an indentifier
#                   help with readability 
#                   order of arguments doesn't matter
#                   1.positional ,2.defualt ,3.keyword,4.arbitrary
def fullname(title,last,name):
    print(f"{title} {name} {last}")
fullname(last="Agrawal",title="Mr.",name="Sudarshan")

# so if we change the position there is no change in our print function
# because we fix the agument with string.
print("1","2","3","4",sep="-")
#this is also the example of keyword argument