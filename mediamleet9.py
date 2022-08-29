def fun(a):
    b=int(input("number::"))
    i=0
    l=[]
    while i<len(a):
        if a[i]==b:
            pass
        else:
            l.append(a[i])
        i=i+1
    print(l)
fun([5,7,5,4,2,6,8,9])