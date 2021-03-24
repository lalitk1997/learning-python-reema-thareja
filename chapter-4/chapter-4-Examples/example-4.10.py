#WAP to determine whether the character entered is vowel or not.

char = str(input("Enter a character : "))
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Vowel : "+str(char))
if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print("Vowel : "+str(char))
else:
    print("Not vowel : "+str(char))
