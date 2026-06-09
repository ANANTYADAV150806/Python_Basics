string = input("enter the string you want to filter:")
words = [word for word in string.split() if word.isalpha()]
first_word = words[0]
vowels = "aeiouAEIOU"
filtered_words = [word for word in words if word[0] in vowels]
consonant_words = [word for word in words if word[-1] not in vowels]
print("the words starting with a vowel in the sting are:", filtered_words)
print("the words ending with a consonant in the string are:", consonant_words)