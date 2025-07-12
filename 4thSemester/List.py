#list  -> list is a mutable data structure
        # we can change its individual element
l1 = [1,2,3,4,5,6,7]
print(type(l1))
print(l1)

l2 = [3,5,4.67,"amit",True,6+9j]
print(l2)
print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])
print(l2[4])
print(l2[5])

print("\n")

# index slicing of list

print(l2[0:4])
print(l2[2:4])
print(l2[0:6:2])
print("\n")

print(l2[::-1]) # reverse for temporary
print(l2)

#change the individual value of list
l2[3] = "vishwaklarma"
print(l2)

print("\n")

l2 = l2[::-1]  # reverse for permanentaly
print(l2)
#print(l2[100])  # error: index out of range



      
