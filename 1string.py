result=input("enter your name: ")

#result=len(result) #it return length of string

#result=result.find(" ") #it find the char from string(only first position)
                         # if there is no space it return -1

#result=result.find("a") #sudarshan it return (3)

#result=result.rfind("a") #sudarshan it return (7) it start form end

#result=result.capitalize() #only first letter get capitalize

#result=result.upper() #capitalize all letter

#result=result.lower()  #it lower all letter

#result=result.swapcase()#it swap the case 
                         #it convert str to upper if it is lower in case vice-versa

#result=result.isdigit()#it return (True) if it contain all number else return (False)
                        #if it contain white spaces so it return False

#result=result.isalpha()#it return (True) if it contain all alphabet else return (False)
                        #if it contain white spaces so it return False

#result=result.count("-")#it count (" - ") in the string 

#result=result.replace("s","a")#it replace ("s") with ("a") in the string

#result=result.strip()#it remove the space only from (start & end)

#result=result.split("#")# it convert string to list(default value is -1)return type list
#result=result.split(maxsplit=-1)#-1 for max limit
#it make (n+1) parts
#it start form left side

#x=["i","love","you"]
#x=" ".join(x)# it convert list to string 
#print(x)

#result=result.split(maxsplit=1)#only differnce is it start form left
#it convert string into 2 part afer one space

#result=result.islower()#it check the string is lower(reutrn true or false)

#result=result.isupper()#it check the string is upper(reutrn true or false)

#result=result.isspace()#it check the string have space(T/F)

#result=result.isnumric()#it check the string have all the number(T/F)

# it is use for all the string function 
#print(help(str))
print(result)