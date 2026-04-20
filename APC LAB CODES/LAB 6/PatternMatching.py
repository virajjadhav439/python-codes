
import re

text = "My birthdate is 06 April"

pattern = r"\d{1,2}\s[A-Za-z]+"
match = re.search(pattern, text)

if match:
    print(match.group())