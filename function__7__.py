#ARBITRARY
# **kwargs =allows you to pass muntiple keyword-arguments 
#           *unpacking operator
#           1.positional ,2.defualt ,3.keyword,4.arbitrary
def address(**kwargs):
    for i,j in kwargs.items():
        print(f"{i:15}:{j}")
    
address(name="Sudarshan Agrawal",
        vila_number="41",
        street="GURU KRIPA DHAM",
        city="MATHURA",
        state="U.P",
        country="INDIA"
        )   
#it behave like dictionary