# all prime number 
print("enter interval to find all prime number")
a = int(input("enter starting number :"))
b = int(input("enter last number :"))
if a == 1:
    print(a)
for i in range(a,b+1):
    flag = False
    for j in range(2,i):
        if i%j == 0:
            flag = True
        if flag == False:
            print(i)
            break
        
            
