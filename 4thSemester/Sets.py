# sets -> indexing of element in set is not possible becoz set store item in random order

s1 = {1,1,1,1,2,2,0,2,3,3,3,"hello","hello","Hello",True,8+8j}
print(type(s1)) #output: set
print(s1)
s2 = {}  
print(type(s2))  #output: dict

#add(item)  -> used to add item into set 
s1.add(6)  
print(s1)    #output: {(8+8j), 0, 1, 2, 3, 6, 'hello', 'Hello'}
s1.add("suman") #output: {0, 1, 2, 3, 6, 'suman', 'hello', 'Hello', (8+8j)}
print(s1)  

#clear() -> clear all the element from sets
s1.clear()  
print(s1)   #output: set()

s1.add("hello")
print(s1)   #output: {'hello'}

# discard(item) -> discard an item fron set.
#               -> (if that element is is not present then it don't give error)
s2 = {1,1,1,1,2,2,0,2,3,3,3,"hello","hello","Hello",True,8+8j}
print("our set is :-",s2)
s2.discard("hello")
print("using discard(item) ='hello'-:",s2)
print("\n")

#remove(item) -> remove an item from set.
#         -> (if that element is is not present then it gives error)
s2.remove(1)
print("using remove(item) = 1 :-",s2)   
print("\n")

#pop() -> this function remove the item from set in randomly
print("our set is :",s2) 
print("removed element :",s2.pop())
print("after removing set is :",s2)
print("removed element :",s2.pop())
print("after removing set is :",s2)
print("removed element :",s2.pop())
print("after removing set is:",s2)
print("\n")

l = [2,2,2,22,4,3,5,4,3]
print("list is : ",l)

# list to set -> call set(list_vaeriable)
s2 = set(l)
print("list to set: ",s2)

# set to list -> call list(set_variable)
l = list(s2)
print("again set to list :",l,"here duplicate element is vanished")
s2 = list(set(l))
print("from list to set and again set to list",s2)

print("\n")

t = (2,2,2,3,3,3,4,44,5,6,7,8,8,8,44)
print("tuple is :",t)
#tuple into set -> call set(tuple_variable)
s3 = set(t)
print("tuple to set",s3)
t = tuple(s3)
print("again set to tuple :",s3,"duplicate elemet is vaniced")
#in sort tuple to set and set to tuple
t1 = (2,2,2,3,3,3,4,44,5,6,7,8,8,8,44)
t1 = tuple(set(t1))
print("fron tuple to set and set to tuple",t1)




