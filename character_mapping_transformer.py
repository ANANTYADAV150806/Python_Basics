string = input("enter the string you want to transform:")
words = string.split()
vowels = "aeiouAEIOU"
shifted_vowels = "eiouAEIOUa"
first_word = words[0]
first_letter = first_word[0]
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shifted = "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA"
if first_letter in vowels:
    vowel_table = str.maketrans(vowels,shifted_vowels)
    new_string = string.translate(vowel_table)
    print("the transformed vowel word is:", new_string)
else:
    alphabet_table = str.maketrans(alphabets , shifted)
    new_alpha = string.translate(alphabet_table)
    print("the transformed constonants word is:", new_alpha )

