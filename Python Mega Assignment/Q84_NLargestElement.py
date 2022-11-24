list1 = [13,5,7,22,56,78,64,31,0,4,9]
final_list =[]
print("Given List:- ",list1)
N = int(input("Enter value for N:-"))

for i in range(0, N):
    max1 = 0    
    for j in range(len(list1)):    
        if list1[j] > max1:
            max1 = list1[j];    
    list1.remove(max1);
    final_list.append(max1)
         
print(final_list)