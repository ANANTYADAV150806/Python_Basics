password = input("enter the password you want to validate:")
if len(password)< 8:
     print("enter atleast 8 chars")
if not any(char.isupper() for char in password):
     print("the password does not contain any uppercase")
if not any(char.islower() for char in password):
     print("the password does not contain any lowercase")
if not any(char.isdigit() for char in password):
     print("the password should contain atleast 1 digit")
if not any(char.isalnum() for char in password):
     print("the password does not contain a special character ")
if " " in password:
     print("there should be no spaces in password")
else :
     print("the password is validate "+ password)
    


