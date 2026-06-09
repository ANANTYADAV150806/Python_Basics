text = input("enter the word you want to process:")
reversed_text = text[::-1]
non_alphanumeric_text = "".join(char.lower() for char in text if char.isalpha())
reversed_non_alphanumeric_text = non_alphanumeric_text[::-1]
if text == reversed_text:
    print("the " + text + " is a normal palindrome")   
if text.lower() == reversed_text.lower():
    print("the " + text + " is a case-insensitive palindrome")
elif non_alphanumeric_text == reversed_non_alphanumeric_text :
    print("the " + text + " is a palindrome ignoring non-alphanumeric characters")
else:
    print("the " + text + " is not a palindrome")


  
