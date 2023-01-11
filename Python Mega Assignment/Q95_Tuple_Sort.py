list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]  
n = len(list)
for i in range(0, n):

    for j in range(0, n-i-1):
        if (list[j][1] > list[j + 1][1]):
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print(list) 