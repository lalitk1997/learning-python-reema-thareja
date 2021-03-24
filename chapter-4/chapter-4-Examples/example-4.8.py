#WAP company offer bonus Male 5% of salary and female 10% of salary. If sal < 10000 extra 2% of salary

sal = float(input("Enter your salary : "))
gen = str(input("Enter gender (m or f) : "))
if sal >= 10000 and gen == 'm':
    print("Salary : "+str(sal + ((5 / 100) * sal)))
if sal < 10000 and gen == 'm':
    print("Salary : " + str(sal + ((7 / 100) * sal)))
if sal >= 10000 and gen == 'f':
    print("Salary : " + str(sal + ((10 / 100) * sal)))
if sal < 10000 and gen == 'f':
    print("Salary : " + str(sal + ((12 / 100) * sal)))
