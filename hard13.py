def fun():
    list=[[1,4,5],[1,3,4],[2,6]]
    l=[]
    for i in list:
        for j in i:
            l.append(j)
            l.sort()
    print(l)
fun()

    
 