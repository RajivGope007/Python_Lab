lst=[1,2,3,4,5]
print("Initial List = ",lst)
t=lst[0]
lst[0]=lst[-1]
lst[-1]=t
print("After swapping List = ",lst)