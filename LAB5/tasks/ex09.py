import re

def insert_spaces_capital(text):
    return re.sub(r'([A-Z])', r' \1', text).strip()

print(insert_spaces_capital("HelloWorld"))  # 'Hello World'
