
import re

text = """Contact us at support@gmail.com or info123@yahoo.co.in
You can also reach admin.test@company.org for queries"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)