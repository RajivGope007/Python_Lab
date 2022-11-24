lst = [1,2,3,4,5,6,7,8,9,10]
print("Given List - ",lst)
a = int(input("Enter first position:-"))
b = int(input("Enter second position:-"))
lst[a-1],lst[b-1] = lst[b-1],lst[a-1]
print("Swapped list- ",lst)