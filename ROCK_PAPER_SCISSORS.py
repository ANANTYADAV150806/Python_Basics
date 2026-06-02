import random

b = [ "rock" , "paper" , "scissors" ]
emojis = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
a = input("enter your choice (rock/paper/scissors):").lower()
c = random.choice(b)
if a not in b:
    print("pls enter a valid input(rock/paper/scissors)")

print(f"you choose {emojis[a]} \nand \ncomputer choose {emojis[c]}")
if a == c:
    print("its a tie!")
elif (a == "rock" and c == "scissors") or (a == "paper" and c == "rock") or (a == "scissors" and c == "paper"):
    print("you win!")
else:
    print("you lose!")
