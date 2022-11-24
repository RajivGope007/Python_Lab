i=n=int(input("Enter a number:-"))
s=r=d=0
#Counting number of digits
while i>0:
    i=i//10
    d+=1
#Armstrong Check
i=n
while i>0:
    r=i%10
    s=s + pow(r,d)
    i=i//10
if s==n:
    print("Armstrong.")
else:
    print("Not Armstrong.")