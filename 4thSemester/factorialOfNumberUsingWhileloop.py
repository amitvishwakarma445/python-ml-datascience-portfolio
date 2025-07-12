#factorial of a given number using while loop

s = input("enter a number :")
n = int(s)
fact = 1
while(n>0):
    fact *=n
    n = n-1
print(fact)
