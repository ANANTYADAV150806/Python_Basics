string = input("enter the string you want to process:")
words = string.split()
k = int(input("enter the length of word you want to find:"))
selected_words = (len(words)) % k
print(selected_words) 

