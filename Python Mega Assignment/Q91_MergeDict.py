def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
     
dict1 = {'Rakesh': 21, 'Suraj': 24, 'Mina': 32}
dict2 = {'Raju': 55, 'Tarun': 29}
dict3 = Merge(dict1, dict2)
print(dict3)