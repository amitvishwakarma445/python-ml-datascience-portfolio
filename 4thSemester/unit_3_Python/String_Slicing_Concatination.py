# stirng is immutable, in python character is not exist 

#declaration of String
s1 = 'String ka Example-1'
s2 = "String ka example-2"
s3 = '''String ka Example-3'''
print(s1) #String ka Example-1
print(s2) #String ka example-2
print(s3) #String ka Example-3

#concatination of string
print(s1+s2) #String ka Example-1String ka example-2
print(s1+s2+s3) #String ka Example-1String ka example-2String ka Example-3

#repeation of String
s4 = "bhai"
print(s4*4) #bhaibhaibhaibhai

#Slicing of String
s5 = "A Quick brown Fox jumps over the lazy dog"
print(s5[5]) #c
print(s5[-3]) #d
print(s5[10:]) #own Fox jumps over the lazy dog
print(s5[10:15]) #own F
print(s5[:15]) #A Quick brown F
print(s5[10:25:2]) #onFxjmso
#reverse String
print(s5[::-1]) #god yzal eht revo spmuj xoF nworb kciuQ A
print(s5[::2]) #AQikbonFxjmsoe h aydg
print(s5[::-2]) #gdya h eosmjxFnobkiQA
print(s5[:-17:-3])#g ae v

