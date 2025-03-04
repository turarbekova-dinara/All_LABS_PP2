def count_lines(file_path):
    try:
        file = open(file_path, "r", encoding="utf-8") 
        lines = file.readlines() 
        file.close() 
        return len(lines) 
    except FileNotFoundError:
        return "Файл табылмады!"  
