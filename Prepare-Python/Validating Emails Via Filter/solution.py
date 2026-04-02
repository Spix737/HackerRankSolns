import re

def fun(s):
    # return True if s is a valid email, else return False
    # Regex explanation:
    # ^                 : start of string
    # [a-zA-Z0-9_-]+    : 1 or more letters, digits, dashes, or underscores (username)
    # @                 : exactly one '@' symbol
    # [a-zA-Z0-9]+      : 1 or more letters or digits (websitename)
    # \.                : exactly one '.' symbol
    # [a-zA-Z]{1,3}     : 1 to 3 letters (extension)
    # $                 : end of string
    
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    pattern_co_uk = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+(\.[a-zA-Z]{1,3}){1,2}$"
    # html5_pattern (<input type="email">) = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

# Open-Source Gold Standard
    # pip install email-validator
    # from email_validator import validate_email, EmailNotValidError

    # def realistic_company_filter(email_address):
    #     try:
    #         # 1. Checks RFC 5322 syntax
    #         # 2. Resolves DNS to check for MX (Mail Exchange) records
    #         # 3. Normalizes the email (lowercases the domain, handles unicode)
    #         valid_email_info = validate_email(email_address, check_deliverability=True)
            
    #         # Returns the perfectly standardized email string
    #         return valid_email_info.normalized
            
    #     except EmailNotValidError as e:
    #         # e.g., "The domain 'fake-domain.com' does not exist"
    #         # e.g., "There is no @ symbol"
    #         print(f"Invalid email: {str(e)}")
    #         return None

    # re.match returns a match object if it fits the pattern, otherwise None
    return bool(re.match(pattern, s))
        

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)