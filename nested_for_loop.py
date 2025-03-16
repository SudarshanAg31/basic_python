#for x in range(1,11,1):
#    for x in range(1,11,1):
#        print(x,end=" ")
#    print()
    
#rectangle
row=int(input("row: "))
col=int(input("col: "))
symbol=input("symbol: ")
for x in range(row):
    for y in range(col):
        print(symbol,end=" ")
    print()