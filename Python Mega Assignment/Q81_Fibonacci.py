n=int(input("Enter postion:- "))
a=c=0
b=1
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    while n>1:
        c=a+b
        a=b
        b=c
        n-=1
    print(c)