import os

def check_path(path):
    if os.path.exists(path):  
        folder = os.path.dirname(path) 
        file = os.path.basename(path) 
        return folder, file 
    return None  


path = "example.txt"
result = check_path(path)

if result:
    print("Folder:", result[0])  
    print("File:", result[1])  
else:
    print("Path does not exist")
