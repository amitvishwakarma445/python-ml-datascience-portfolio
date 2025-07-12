# if string has n number of element then
# in string the indexing is from 0 to n-1 and 
# and in reverse manner the indexing is from -1 to -n

s = "vishwakarma"

# length of string
print(len(s))

# individual character

print(s[0])  # v
print(s[1])  # i
print(s[2])  # s
print(s[3])  # h
print(s[4])  # w
print(s[5])  # a
print(s[6])  # k 
print(s[7])  # a
print(s[8])  # r
print(s[9])  # m
print(s[10]) # a

print("\n")

print(s[-1])  # a
print(s[-2])  # m
print(s[-3])  # r
print(s[-4])  # a 
print(s[-5])  # k
print(s[-6])  # a
print(s[-7])  # w
print(s[-8])  # h
print(s[-9])  # s
print(s[-10]) # i
print(s[-11]) # v

print("\n")

# index slicing
print(s[0:3])     # vis
print(s[0:12:2])  # vswkra
print(s[::2])     # vswkra
print(s[6:12])    # karma
print(s)          # vishwakarma
print(s[::-1])    # amrakawhsiv
print(s[-1:-12:-1])# amrakawhsiv



        
        
            
