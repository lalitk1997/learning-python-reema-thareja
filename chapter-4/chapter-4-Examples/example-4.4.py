#WAP to determine whether a person is eligible to vote? In case of not-eligible,
#display how many years are left to be eligible.

age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Wait "+str(18 - age)+" year until, you become 18.")

