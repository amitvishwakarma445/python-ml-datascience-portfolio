# all prime number 
a = int(input("enter a number :"))
flag = True
for i in range(2,a):
    if a%i == 0:
        flag = False
        if flag == True:
            print(a,"is prime number")
        else:
            print(a,"is not prime number")
        break
