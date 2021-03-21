#WAP to print distance between (x1,y1) - (x2, y2)
x1 = int(input("Enter value of x1 :"))
y1 = int(input("Enter value of y1 :"))
x2 = int(input("Enter value of x2 :"))
y2 = int(input("Enter value of y2 :"))
dist = (((x2-x1)**2)+((y2-y1)**2))**0.5
print("Total distance : "+str(dist))