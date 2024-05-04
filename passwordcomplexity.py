import re

def get_password_strength(password):
    # Check password length
    length_score = min(len(password) / 8, 1)  # Normalize length to a score between 0 and 1
    
    # Check character types
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check if all character types are present
    all_types_present = all([has_uppercase, has_lowercase, has_digit, has_special])
    
    types_score = 1 if all_types_present else 0  # Set types_score to 1 if all types are present, else 0
    
    # Determine missing character types
    missing_types = []
    if not has_uppercase:
        missing_types.append("uppercase letters")
    if not has_lowercase:
        missing_types.append("lowercase letters")
    if not has_digit:
        missing_types.append("digits")
    if not has_special:
        missing_types.append("special characters")
    
    # Calculate overall strength score
    strength_score = (length_score + types_score) / 2
    
    return strength_score, missing_types


def get_feedback(strength_score):
    if strength_score >= 0.75:
        return "Strong"
    elif strength_score >= 0.5:
        return "Moderate"
    else:
        return "Weak"

# Continuous loop until password meets complexity criteria
while True:
    password = input("\nEnter your password: It's length must be at least 8 and contain Uppercase, Lowercase, number, and special character\n")
    strength_score, missing_types = get_password_strength(password)
    
    if strength_score >= 0.8:  # Modify the threshold as desired
        print("Password is strong")
        break
    
    print("Password is too weak. \nPlease choose a stronger password.")
    
    if missing_types:
        print("The following character types are missing:", ', '.join(missing_types))
