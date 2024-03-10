import re

string = "Please contact 'info@example.com' for assistance. Phone: (123) 456-7890 or (111) 222-3333" 
    

    # Extracts phone numbers from a given strings
def extract_phone_numbers(string):
    
    # Define regex pattern for phone numbers
    pattern = re.compile(r'^(\+\d{3}\s?)?((\(\d{3}\)|\d{3}))[\s.-]?\d{3}[\s.-]?\d{4}$')
    
    # find all matches of pattern in string
    matches = pattern.findall(string)
    
    return matches
    
    # extracts email addresses from a given string
def extract_email_addresses(string):
    
    # define a regex pattern for email addresses
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+")
    
    # find all matches in the string
    matches = pattern.findall(string)
    
    return matches


    # replaces email addresses in the given string with a replacement string
def replace_email_addresses(string, replacement) :
    
    # define a regex pattern for email addresses
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+")
    
    # use re.sub() to replace email addresses in given string with a rep string
    output = pattern.sub(replacement, string)
    
    return output

replacement = "***REDACTED***"
print(extract_phone_numbers(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, replacement))
    
    
# ^ - Start of the line.
# (\+\d{1,2}\s)? - Optional country code (e.g., +1 or +11).
# \(?\d{3}\)? - Optional area code enclosed in parentheses.
# [\s.-]\d{3} - A separator (space, dot, or hyphen) followed by three digits.
# [\s.-]\d{4} - A separator followed by four digits.
# $ - End of the line.  
    
  