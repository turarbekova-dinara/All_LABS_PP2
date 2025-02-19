import re

def find_upper_followed_lower(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)

print(find_upper_followed_lower("Hello World Example Test"))  # ['Hello', 'World', 'Example', 'Test']
