#python writing files (.txt,.json,csv)
#"w" (Write):-Creates a new file if it doesn't exist. Overwrites the file if it already exists.
#"x" (Exclusive Creation):-Creates a new file but fails with an error if the file already exists.
#"a" it is use to append data to exist file.
tex_data="i like pizza "
file_path="C:\\Users\\Lenovo\\OneDrive\\Desktop\\output.txt"
with open(file_path,"w") as file:
    file.write("\n"+tex_data)
    print("file created")
    
print("Example 2")

name=["sudarshan","love","tanvi","dhruv"]
file_pth="C:\\Users\\Lenovo\\OneDrive\\Desktop\\name.txt"
with open(file_pth,"w") as file:
    for i in name:
        file.write(i+"\n")
    print("file is created")
#NOTE:we use for loop to get all the name in our file