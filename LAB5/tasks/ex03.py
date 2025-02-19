import re

def find_lowercase_underscore(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

print(find_lowercase_underscore("hello_world example_test"))  # ['hello_world', 'example_test']
