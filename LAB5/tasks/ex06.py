import re

def replace_special_chars(text):
    return re.sub(r'[ ,.]', ':', text)

print(replace_special_chars("Hello, World. Python is great"))  # 'Hello:World:Python:is:great'
