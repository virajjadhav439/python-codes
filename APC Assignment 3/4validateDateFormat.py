import re

def validate_date(date):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"
    
    if re.match(pattern, date):
        return "valid"
    else:
        return "invalid"


# Example
date = input("Enter date (DD-MM-YYYY): ")
print(validate_date(date))