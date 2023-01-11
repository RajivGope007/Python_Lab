string = "I write code."
print("Give String:- ",string)
while 1:
    pos = int(input("Enter index to remove:- "))
    if pos>=len(string):
        print("Please Enter Correct Index.")
    else:
        break
new_str = string[:pos-1] + string[pos:]
print("New String:- ",new_str)