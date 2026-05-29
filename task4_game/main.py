import random

choices = ["rock", "paper", "scissors"]

user_score = 0
pc_score = 0

while True:

    user = input("Choose Rock/Paper/Scissors: ")

    pc = random.choice(choices)

    print("Computer:", pc)

    if user == pc:
        print("Draw")

    elif (
        (user == "Rock" and pc == "Scissors") or
        (user == "Paper" and pc == "Rock") or
        (user == "Scissors" and pc == "Paper")
    ):
        print("You Win")
        user_score += 1

    else:
        print("Computer Wins")
        pc_score += 1

    print("Score:", user_score, "-", pc_score)

    again = input("Play Again? y/n: ")

    if again.lower() != "y":
        break