import re

text = "I love Python"
result = re.search(r"love Python", text)

if result:
    print("Found:", result.group())