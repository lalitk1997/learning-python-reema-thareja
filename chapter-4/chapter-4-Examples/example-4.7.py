#WAP to get any character -> converts lower i/p to upper & ipper to lower

char = str(input("Enter the character : "))
if char.isupper():
    print("Upper Character."+str(char.lower()))
if char.islower():
    print("Lower Character."+str(char.upper()))