n = int(input("Enter a number:- "))
i=2
n=2
while i< n/2:
    if n%i == 0:
        break
    else:
        i+=1
if i>n/2 :
    print(n," is a Prime Number.")
else:
    print(n," is a Not Prime Number.")