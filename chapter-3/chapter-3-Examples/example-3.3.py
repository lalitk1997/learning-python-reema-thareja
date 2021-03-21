#WAP to calculate area of a triangle using herons formula
s1 = float(input("Enter side-1 value :"))
s2 = float(input("Enter side-2 value :"))
s3 = float(input("Enter side-3 value :"))
s = (s1+s2+s3) / 2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print("Area of the triangle is :"+str(area))
