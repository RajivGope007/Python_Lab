string = "The quick brown fox jumps over the lazy dog."
print("Give String:- ",string)
k = int(input("Enter the length:-"))
words = string.split(" ")
final_words=[]
for i in words:
    if len(i)>k:
        final_words.append(i)
print("Words having length greater than",k," are:- ",final_words)