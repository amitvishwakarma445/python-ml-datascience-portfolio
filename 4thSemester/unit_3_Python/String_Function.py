s = "abc defGhi Klm"
#1. capitalize()-> capitalize the first character of string
s1 = s.capitalize()
print(s1) #Abc defGhi Klm

#2. upper()-> change into upper case
s2 = s.upper()
print(s2) #ABC DEFGHI KLM

#3. lower()-> change into lower case
s3 = s.lower()
print(s3)

#4. title()-> convert every first letter of words into capital letter
s4 = s.title()
print(s4) #Abc Defghi Klm

#5. length()
print(len(s))

#6. center()
print(s.center(24)) #     abc defGhi Klm     
print(s.center(24,"x")) #xxxxxabc defGhi Klmxxxxx

#7. count()-> count occurance(repeatation) of any subString 
s5 = "abc dhaf hrkabdh"
print(s5.count("O")) #0
print(s5.count("a")) #3
print(s5.count("ab")) #2
print(s5.count("a",4)) #2

print("\n")
#8. find()-> find the index of Any subString, in case not present, return -1
print(s5.find("a")) #0
print(s5.find("z")) #-1
print(s5.find("af")) #7
print(s5.find("a",2)) #6
print(s5.find("a",7)) #12

print("\n")
#9. index()-> find of any subSting, in case of not present, gives error and terminate program
print(s5.index("a")) #0
#10. print(s5.index("z")) #ValueError: substring not found
print(s5.index("af")) #7
print(s5.index("a",2)) #6
print(s5.index("a",7)) #12

#11. starstwith() -> return boolean value if Substring start with given SubString
print(s5.startswith("ab")) #True
print(s5.startswith("ac")) #False

#12. endswith() -> return boolean value if Substring end with given SubString
print(s5.endswith("bdh")) #True
print(s5.endswith("Bdh")) #False
print(s5.endswith("ac")) #False

#13. Join()->
s6 = ["abc","def","ghi"]
s7 = "123"
print(s7.join(s6))

#14. max()-> gives maximum ascii value character
s8 = "ABC"
print(max(s8))
#14. min()-> gives minimum ascii value character
print(min(s8))

#14. ljust()
print(s8.ljust(4,"x")) #ABCx
print(s8.ljust(7,"x")) #ABCxxxx

#15. rjust()
print(s8.rjust(4,"x")) #xABC
print(s8.rjust(7,"x")) #xxxxABC

s9 = "  amit  "
print("X",s9,"X") 
#16. rstrip()-> remove space from right hand side
print("X",s9.rstrip(),"X")
#17. lstrip()->remove space from left hand side
print("X",s9.lstrip(),"X")
#18. strip()->remove space from both sides
print("X",s9.strip(),"X")
print(s9.strip())

#19. replace()-> replace a part of string to other String
s10 = "good Morning"
print(s10)
print(s10.replace("Morn","Even"))


#Escape Sequence Character
#. \\
s11 = "Example of \\n Escape Sequence character"
print(s11)
#2. \n
s12 = "Example of \nEscape Sequence character"
print(s12)
#3. \b
s13 = "Exam\bple"
print(s13) #m will not print out[ut:Exaple
#4. \r
s14 = "Example\rabc"
print(s14) #output: abcmple
s15 = "Example\tabc"
print(s15) #Example	abc

