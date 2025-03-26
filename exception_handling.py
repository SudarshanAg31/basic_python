#exception:An event that interrupts the flow of a program
#          (ZeroDivisionError,TypeError,ValueError)
#           1.try   2.except    3.finally
try:
    number=int(input("enter number:"))
    print(1/number)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("Enter only number plz")
except Exception:
    print("someting went wrong!")
finally:
    print("Do some cleanup here")
#NOTE:try block is use for because user can enter any thing 
#so, for that code run properly we use try except
#NOTE:finally block is run in every situation
    