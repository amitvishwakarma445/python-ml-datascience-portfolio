#Armstrong number 

n = int(input("enter a number:"))
temp = n
armstrong = 0
while n>0:
    lastDigit = n%10
    cube = lastDigit**3
    armstrong += cube
    n //= 10
if temp == armstrong:
    print(temp,"is a armstorng number")
else:
    print(temp,"is not a armstrong number")
