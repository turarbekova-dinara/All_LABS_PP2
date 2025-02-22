import re

def match_a_anything_b(text):
    return bool(re.fullmatch(r'a.*b', text))

print(match_a_anything_b("acb"))  # True
