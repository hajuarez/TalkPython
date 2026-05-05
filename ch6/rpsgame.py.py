import random

print("--------------------------------")
print("Rock Paper Scissors v1")
print("--------------------------------")

player_1 = "You"
player_2 = "Computer"

rolls = ["rock", "paper", "scissors"]

roll1 = input(f"{player_1}, enter your roll [rock, paper, scissors]: ")
roll1 = roll1.lower().strip() # Convert to lowercase to make it case-insensitive
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} is not a valid play!")

#2nd player automated, no need to validate input
roll2 = random.choice(rolls)

print(f"{player_1} rolls {roll1}")
print(f"{player_2} rolls {roll2}")

#Test for a winner
# Rock
#   Rock -> tie
#   Paper -> lose
#   Scissors -> win
# Paper
#   Rock -> win
#   Paper -> tie
#   Scissors -> lose
# Scissors
#   Rock -> lose
#   Paper -> win
#   Scissors -> tie

winner = None

if roll1 == roll2:
    print("It's a tie!")
elif roll1 == "rock":
    if roll2 == "scissors":
        print(f"{player_1} wins!")
    else:
        print(f"{player_2} wins!")
elif roll1 == "paper":
    if roll2 == "rock":
        print(f"{player_1} wins!")
    else:
        print(f"{player_2} wins!")
elif roll1 == "scissors":
    if roll2 == "paper":
        print(f"{player_1} wins!")
    else:
        print(f"{player_2} wins!")



