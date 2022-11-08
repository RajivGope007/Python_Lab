x = int(input("Enter First Number:- "))
y = int(input("Enter Second Number:- "))
z = int(input("Enter Third numbers:- "))
if x>y and x>z :
    print("{} is greater.".format(x))
elif y>x and y>z:
    print("{} is greater.".format(y))
elif z>x and z>y:
    print("{} is greater.".format(z))
else:
    print("All are equal.")
