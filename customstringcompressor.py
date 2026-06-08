from collections import Counter
word = input("enter the string you want to compress:").lower()
letter_counts = Counter(word)
output = "".join(f"{letter}{count}" for letter, count in letter_counts.items())
print("the output is:" , output)