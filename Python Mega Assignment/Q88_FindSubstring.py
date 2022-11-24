string = "I write code."
print("Give String:- ",string)
substring = input("Enter Substring to search:-\n")
if substring in string:
    print("Found")
else:
    print("Not Found")
