import re

def snake_to_camel(text):
    return ''.join(word.title() if i > 0 else word for i, word in enumerate(text.split('_')))

print(snake_to_camel("hello_world"))  # 'helloWorld'
