# logical operator:evaluate multiple conduction(or,and,not)..
# or:- use to check multiple conduction if any one is true so it run..
# and:- use to check multiple conduction if all the conduction is true then it run our code
# not:- it inverts the conduction(not True, not False)

#or
x=100
myfriend=True
if x<40 or x>0 or myfriend:
    print("you may go...")
else:
    print("sorry :(")
#and
x=-5
myfriend=True
if x<40 and x>0 and myfriend:
    print("you may go...")
else:
    print("sorry :(")
#not
myfriend=False
if not myfriend:
    print("you may go...")
else:
    print("sorry :(")