a = input("enter a sentence that you want to analyze:")
words = a.split()
longest_word = max(words, key=len)
reversd_words = [word[::-1] for word in words]
output_sentence = " ".join(reversd_words)
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0 
for char in a:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1
    elif char.isdigit():
        digit_count +=1
print("the longest word in the sentence is:" , longest_word)
print("reversed sentence:" , output_sentence)
print("vowel count:" , vowel_count)
print("consonant count:" , consonant_count)
print("digit count:" , digit_count)