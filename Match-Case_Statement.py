#Match case statement(switch):An alternative to using many 'elif' statements
#                             Execute some code if a value matches a 'case' 
#                             Benefits: cleaner and syntax is more readable
def day_in_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case 8:
            return "it is not valid day"
print(day_in_week(1))
#NOTE:we can pass string 

       