def fun ():
    a=int(input("enter any num::"))
    p=0
    x=a
    while a>0:
        p=p*10+a%10
        a=a//10
    if (x==p):
        print("palindrome",p)
    else:
        print(" not palindrome",p)
fun()