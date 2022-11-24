lst = [10, 20, 30, 40, 50, 60]
print("Initial List:- ",lst)
s=j=0
final_list=[]
for i in range(1,len(lst)+1):
    for j in range(0,i):
        s+=lst[j]
    final_list.append(s)
    s=0;
print(final_list)
