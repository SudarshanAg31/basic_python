file_path="C:\\Users\\Lenovo\\OneDrive\\Desktop\\name.txt"
with open(file_path,"r") as file:
    a=file.read()
    print(a)    
    
print("Example 2")

import json
file_p="C:\\Users\\Lenovo\\OneDrive\\Desktop\\json.json"
with open(file_p,"r") as file:
    a=json.load(file)
    print(a)#for whole dictionary
    #---or---
    print(a["age"])# for single key and value