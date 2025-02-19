import re

def match_a_b_exact(text):
    return bool(re.fullmatch(r'a{1}b{2,3}', text))

print(match_a_b_exact("abb"))  # True
