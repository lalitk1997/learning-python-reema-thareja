#WAP to convert a lower-case letter to upper-case
char = input("Enter a lower-case letter : ")
print("Lower-case letter : "+str(char))
char_upper = chr(ord(char) - 32)
print("Upper-case letter : "+str(char_upper))
