# for json
import json
emp={"name":"Sudrshan",
     "age":19,
     "job":"IT"}
emp_path="C:\\Users\\Lenovo\\OneDrive\\Desktop\\json.json"
with open(emp_path,"w") as file:
    json.dump(emp,file,indent=4)
    print("json file is created")