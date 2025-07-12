s = input("enter a number :")
n = int(s)
Sum = 0
while(n > 0):
    lastDigit = n%10
    Sum = Sum + lastDigit
    n= n // 10
print(Sum)
