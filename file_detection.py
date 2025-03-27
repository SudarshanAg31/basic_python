import os
#os module is use to intrect with computer system
file_path="C:/Users/Lenovo/OneDrive/Desktop/coding/python language/python-file/basic python/test"
if os.path.exists(file_path):#.exist use for that any (file or folder) is exists or not 
    print("yes it exist")
    if os.path.isfile(file_path):# only for file
        print("file exist")
    elif os.path.isdir(file_path):#only for folder 
        print("folder exist")
else:
    print("no")