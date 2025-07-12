def f1 (**d):
    for key in d:
        val = d[key]
        print(key,"=",val)
    print(d)
    
f1(x=10,y=20)