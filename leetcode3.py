def fun(num):
    i=0
    num=int(input("enetr any num::"))
    while num<0:
        sign=-1
        num=num*-1
    while num>0:
        i=i*10+num%10
        num=num//10
    print("reverse num",i)
fun(123)