import random

a = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    try:
        g = int(input("enter your guess:"))
        if g<0 or g>100:
            print("pls enter number between 1 to 100")
            continue
        if g < a:
            print("too low! try again")

        elif g > a:
            print("too high! try again")

        else:
            print("congratulations! you guessed it right!")
            break
    except ValueError:
        print("pls enter a valid whole number")      