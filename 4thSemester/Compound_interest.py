#Compound interest

p = int(input("enter principle :"))
r = int(input("enter rate :"))
t = int(input("enter time :"))
amount = p*(pow((1+r/100),t))    # amount = p*(1+r/100)**t
compound_interest = amount - p
print(compound_interest);
