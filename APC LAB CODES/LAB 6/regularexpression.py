# # searching 

# import re

# text = "abc123"

# m = re.search(r"\d+", text)

# print(m.group())

## find all 

# import re

# text = "abc123xyz456"

# print(re.findall(r"\d+", text))

# # split()

# import re

# text = "apple,banana;orange"

# print(re.split(r"[,;]", text))

## sub()

# import re

# text = "a1b2"

# print(re.sub(r"\d", "X", text))


## regular expression question 

import re

text = "Today date is 18-03-2026"

match = re.search(r"(\d{2})-(\d{2})-\d{4}", text)

print(match.group(1)) 
print(match.group(2))  


## fetch the all 

import re 

string = "hello my number is 64565675 and my freind number 85767458"

regex= r"\d+"

match = re.findall(regex,string)
print(match)



## find pattern 