def number(a):
    r=int(input("enter any num::"))
    for i in range(len(a)):
        if a[i]==r:
            return i
        else:
            pass
          
print(number([1,7,9,3,0]))

