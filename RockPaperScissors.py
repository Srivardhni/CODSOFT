# RockPaperScissors

import random

uc = 0  # user's count
cc = 0  # Comptuer's count

while True:

    op = ["Rock", "Paper", "Scissors"]
    comp = random.choice(op)

    user = input("Enter Rock, Paper or Scissors:  ")
    print("Computer's choice is", comp)

    if comp == user:
        print("It's a tie")
    elif comp == "Rock" and user == "Scissors":
        print("Rock beats Scissors")
        print("Computer wins")
        cc += 1
    elif comp == "Scissors" and user == "Paper":
        print("Scissors beats paper")
        print("Computer wins")
        cc = +1
    elif comp == "Paper" and user == "Rock":
        print("Paper beats Rock")
        print("Computer wins")
        cc += 1

    elif user == "Rock" and comp == "Scissors":
        print("Rock beats Scissors")
        print("User wins")
        uc += 1
    elif user == "Scissors" and comp == "Paper":
        print("Scissors beats paper")
        print("User wins")
        uc += 1
    elif user == "Paper" and comp == "Rock":
        print("Paper beats Rock")
        print("User wins")
        uc += 1

    again = input("Replay game? (y/n):  ").lower()
    if again != "y":
        print("Thankoos for playing broski")
        print("User score=", uc)
        print("Computer score=", cc)
        break
# print("User score=", uc)
# print("Computer score=", cc)
