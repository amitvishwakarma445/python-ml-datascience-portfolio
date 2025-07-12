#*****list  -> list is a mutable data structure
# we can change its individual element
l = [1,6.43,"hello",True,9+5j]
print(type(l))

print("\n")

# ***** for string
s = "amit "
print(s*3)
# output: amit amit amit
print("\n")

#***** for List
print(l*2)    # output: [1,6.43,"hello",True,9+5j,1,6.43,"hello",True,9+5j]
print("\n")

#***** concatination of list -> List can concate only List
print('concatination of list -> List can concate only List')
l1 = [1,2,"bhai",False]
print(l + l1)
print("\n")

#***** length of String
print('length of String')
print(len(l))
print(len(l1))
print("\n")

#*****element search in List   -> output: bool value
print('element search in List   -> output: bool value')
print("hello" in l)
# or
x = "bhai" in l1
print(x)
print("\n")

#***** maximum value in List  -> list contain only either real number or String
print("maximum value in List  -> list contain only either real number or String")
l2 = [2,3,6,3.78,5,9,7,5,56,65,3,44,56]
print(l2)
n = max(l2)
print("max = ",n)
m = min(l2)
print("min = ",m)
print("\n")

l3 = ["amit", "suman", "sumit", "manish", "sheetal"]
print(l3)
print("max = ",max(l3))
print("min = ",min(l3))
print("\n")

l4 = [True, False]
print("max of bool = ",max(l4))    # true
print("\n")

#***** append function  -> used to append individual element into List
print('# append function  -> used to append individual element into List in the last')
l5 = [1,"bhai",True,6+7j]
print(l5)
l5.append(12)
l5.append("manish")
l5.append(True)
print(l5)

print("\n")

#****** insert function -> used to insert element at the specific index
print("# insert function -> used to insert element at the specific index")
l6 = [1,3.45,"hello",True,6+7j]
print(l6)
l6.insert(1,456)
#print(l6)
l6.insert(0,"bharati")
print(l6)
l6.insert(3,False)
print(l6)
print("\n")

#****** pop function -> used to pop the element from list
print("# pop function -> used to pop the last element from list")
l7 = [3,6,"hello", True, 8+8j]
print(l7)
l7.pop()  # by default remove the last element from List
print(l7) 
l7.pop(2)  # remove 2nd index element
print(l7)
print("\n")

# ***** reverse function -> permanently reverse the list
print("# reverse function -> permanently reverse the list")
l8 = [1,3.45,"hello",True,6+7j]
print(l8)
l8.reverse()
print(l8)
print("\n")

#****** sort function -> used to sort an list in ascending order
#               list must contain either only real value or string
print("# sort function -> used to sort an list in ascending order")
print("# list must contain either only real value or string")
print(l2)
l2.sort() # arrange in ascending order
#l2.sort(reverse=False)
print(l2)
l2.sort(reverse=True) # arrange in descending order
print(l2)
print("\n")
print(l3)
l3.sort()
l3.sort(reverse=True)
print(l3)

# *****nested list (list into list )
l9 = [15,"sheetal", 6.75, True]
l10 = [16,"amit", 16.75, False]
l11 = [l9,l10,"Hello",8+8j]
print(l11)   #output: [[15,'sheetal', 6.75, True], [16, 'amit', 16.75, False], 'Hello', (8+8j)]
print(l11[0])#output: [15, 'sheetal', 6.75, True]
print(l11[1])#output: [16, 'amit', 16.75, False]
print(l11[2])#output: Hello
print(l11[3])#output: 8+8j
print(l11[0][1])#output: sheetal
print(l11[1][1])#output: amit

ls1 = [3,4,8,5,4,3]
ls2 = [6,7,8]
ls1.extend(ls2)
print(ls1)
for item in ls1:
    print(ls1[item],end=",")