import re

text = "I love Java"
new_text = re.sub(r"Java", "Python", text)

print(new_text)