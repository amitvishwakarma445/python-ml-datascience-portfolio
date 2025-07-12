# tuple ->  are mutable entity like String

t = ()
print(type(t))

# print individual element fron tuple
t1 = (1,3,4.5,"hello",True)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])
# Hense selection of individual element from list and tuple are same

#change of individual element in tuple
#t1[5] = False  error: 'tuple' object does not support item assignment
# hense in tuple we can not change element of tuple as string

# convert tuple into list
l1 = list(t1)
print(type(l1))

# convert list into tuple
t1 = tuple(l1)
print(type(t1))

#count function -> used to cound total no of element present in tuple
t2 = (1,2,2,2,3,3,4,4,44.6,True, True)
n = t2.count(4)
m = t2.count(2)
p = t2.count(1)
print("total no of: 4 =", n)
print("total no of: 2 =", m)
print("total no of: 1 =", p)
print("total no of: 100 =", t2.count(100))
print("total no of: False =", t2.count(False))

#index function -> show the (least) index of particular element
print(t2.index(1))
print(t2.index(2))
print(t2.index(3))
print(t2.index(4))
print(t2.index(44.6))
# print(t2.index(100))  error: 100 not in tuple

# minimum and maximum element in tuple
t3 = (3,4,5,8,2,-3,4,1,23,44,5,7)
m = min(t3)
n = max(t3)
print("min = ",m,"max = ",n)

# length of tuple
print(len(t3))
