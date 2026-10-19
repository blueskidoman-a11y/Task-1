import re

def check_password_strength(password):
    # Check minimum length of 8 characters
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase and lowercase letters
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return "Moderate: Include both uppercase and lowercase letters."
    
    # Check for numbers
    if not re.search(r"\d", password):
        return "Moderate: Include at least one number."
    
    # Check for special characters
    if not re.search(r"[@$!%*?&]", password):
        return "Moderate: Include at least one special character."
    
    return "Strong: Your password meets all security requirements!"

if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    print(check_password_strength(pwd))