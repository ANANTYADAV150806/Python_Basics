import random

while True:
    a = input("Roll the dice? (yes/no) :").lower()
    if a == "yes":
        try:
            b = int(input("how many dice you want to roll ?"))
            if b <= 0:
                print("pls enter number greater than 0 ")
                continue
            
            rolls = []
            for i in range(b):
                roll =random.randint(1, 6)
                rolls.append(roll)
            print(f"You rolled {b} dice: {rolls}")
        except ValueError:
            print("pls enter a valid whole number")
    elif a == "no":
        print("ok, maybe next time!")
        break
    else:
        print("invalid input, please enter yes or no.")
