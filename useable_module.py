from datetime import datetime
import re

def verify_date(date_str):
    try:
        # Try to parse the date string to the format YYYY-MM-DD
        date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Check if the date is in the past (optional depending on your use case)
        if date >= datetime.now():
            return False
        
        return True
    except ValueError:
        # If parsing fails, it's an invalid date format or an impossible date
        return False

def verify_email(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def is_valid_string(s):
    if (s=="" and "Null" not in s):
        return False
                
    else:
        for char in s:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

def verify_mobile_number(number):
    if number.isdigit():
        if len(number)==10:
            return True
        else:
            return False
    else:
        return False

def verify_address(address):
    if address is not None:
        if len(address)>=10:
            return True
        else:
            return False
    else:
        return False
