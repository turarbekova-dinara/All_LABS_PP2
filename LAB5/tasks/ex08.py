import re

def split_uppercase(text):
    return re.split(r'(?=[A-Z])', text)

print(split_uppercase("HelloWorldExample"))  # ['Hello', 'World', 'Example']
