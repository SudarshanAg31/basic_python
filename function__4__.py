#DEFAULT ARGUMENTS: a default value for certain parameters 
#                   default is used when that argument is omitted
#                   make your function more flexible , reduces # of arguments
#                   1.positional ,2.defualt ,3.keyword,4.arbitrary

#so we set default value of discount and tax
def net_price(price,discount=.1,tax=0.05):
    return price *(1-discount)*(tax+1)
print(net_price(500))
print()
print("EXAMPLE:-2")
#example:-2
import time
def count (end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Done!")
count(10)
#NOTE= if we set a defult value in our function 
# so we set positional as first then deafult 