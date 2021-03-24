#WAP to determine the character entered by user.

char = str(input("Enter a character : "))
if char.isalpha():
    print("Character is alphanumeric.")
if char.isdigit():
    print("Character is digit.")
if char.isspace():
    print("Character is space.")