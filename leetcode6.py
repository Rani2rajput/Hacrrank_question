def fun():
    a=[1,3,2]
    b=[4,6,5]
    i=0
    while i<len(b):
        a.append(b[i])
        i=i+1
    a.sort()
    print(a)
fun()
