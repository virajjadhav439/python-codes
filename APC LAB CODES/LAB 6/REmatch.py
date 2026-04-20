import re

text = "Hello World"
result = re.match(r"Hello", text)

if result:
    print("Match Found")
else:
    print("Match not Found")