
import re

text = "My marks are 85, 90 and 78"
numbers = re.findall(r"\d+", text)

print(numbers)