#WAP to calculate the bill amount for an item given its quantity sold, value, discount, and tax.
qty = int(input("Enter total quantity :"))
val = float(input("Enter the value per item :"))
discount = float(input("Enter total discount percentage :"))
tax = float(input("Enter total tax percent on cost price :"))
tot_amt = qty * val
print("Cost-Price : "+str(tot_amt))
tot_amt_disc = float(tot_amt-(qty * val * (discount / 100)))
print("Cost-price after discount : "+str(tot_amt_disc))
tot_amt_disc_tax = float(tot_amt_disc + (tot_amt_disc * (tax / 100)))
print("Cost-price after discount and tax addition :"+str(tot_amt_disc_tax))

