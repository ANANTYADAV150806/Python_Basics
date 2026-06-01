import random

while True:
    a = input("Roll the dice? (yes/no) :").lower()
    if a == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1},{dice2})')
    elif a == "no":
        print("ok, maybe next time!")
        break
    else:
        print("invalid input, please enter yes or no.")
