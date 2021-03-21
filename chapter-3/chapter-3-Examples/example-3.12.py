#WAP to calculate the amount of money in piggy bank, denomination of rupees 10, 5, 2, 1.
money_tot = int(input("Enter total amount of money : "))
count_10 = 0
count_5 = 0
count_2 = 0
count_1 = 0
while money_tot >= 10 :
    count_10 = count_10 + 1
    money_tot = money_tot - 10
while money_tot < 10 & money_tot > 5:
    count_5  = count_5 + 1
    money_tot = money_tot - 5
while money_tot < 5 & money_tot > 2:
    count_2 = count_2 + 1
    money_tot = money_tot - 2
while money_tot <= 1  & money_tot > 0:
    count_1 = count_1 + 1
    money_tot = money_tot - 1
print("10 : "+str(count_10)+" 5 : "+str(count_5)+" 2 : "+str(count_2)+" 1 : "+str(count_1))

