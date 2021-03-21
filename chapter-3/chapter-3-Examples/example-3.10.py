#WAP to print average of two numbers , also print their deviation.
num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
avg = (num1 + num2)/2
dev1 = num1 - avg
dev2 = num2 - avg
print("Average of two numbers : "+str(avg))
print("Deviation of num1 : "+str(dev1))
print("Deviation of num2 : "+str(dev2))
