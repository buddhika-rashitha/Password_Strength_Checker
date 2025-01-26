# DA-108 : Python Programming - week 03
# Password Strength Checker

import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "█ Password Strength Checker █" # Special Character (Full Block - Unicode code point - U+2588)
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)
print(linebreak)

while True:
    # Take user input
    password = input("Enter a password: ")

    # Initialize checks for password criteria
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Special characters stored in a list
    special_characters = ["@","#","$","%","^","&","*","(",")","_","+","!","-","+","=","~","`","<",">","?","/",".",",",":",";","[","]","{","}","\\","|"]

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Check the length of the password and determine strength
    if len(password) < 6:
        print(linebreak)
        print("Weak password. Password is too short. Try using at least 6 characters.")
        print(linebreak)
    elif has_upper and has_lower and has_digit and has_special:
        print(linebreak)
        print("Strong password! Great job!")
        print(linebreak)
        break
    elif has_upper or has_lower and has_digit:
        print(linebreak)
        print("Medium password. Try adding Special Characters for a Stronger Password.")
        print(linebreak)
    else:
        print(linebreak)
        print("Weak password. Try using a mix of Uppercase, lowercase, Numbers, and Special Characters.")
        print(linebreak)
