import re

def validate_registration(reg):
    pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{3}$"
    
    if re.match(pattern, reg):
        return True
    else:
        return False