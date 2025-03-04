def write_list_to_file(file_path, data):
    file = open(file_path, "w", encoding="utf-8") 
    for item in data:  
        file.write(item + "\n") 
    file.close() 

my_list = ["Apple", "Banana", "Cherry", "Date"] 
file_path = "output.txt" 

write_list_to_file(file_path, my_list) 
print("Тізім файлға жазылды!") 
