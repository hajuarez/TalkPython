import random

def main():
    show_header()
    play_game("You", "Computer")

def show_header():
    print("--------------------------------")
    print("Rock Paper Scissors v1")
    print("--------------------------------")

def play_game(player_1, player_2):
    rolls = ["rock", "paper", "scissors"]

    roll1 = get_roll(player_1, rolls)
    #roll2 = get_roll(player_2, rolls)
    roll2 = random.choice(rolls)                #2nd player automated, no need to validate input

    if roll1 is None:
        print("Can't play that, exiting!")
        return

    print(f"{player_1} rolls {roll1}")
    print(f"{player_2} rolls {roll2}")

    winner = determine_winner(roll1, roll2, player_1, player_2)
    if winner is None:
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

def determine_winner(roll1, roll2, player1, player2):
    # Rules:
    # Rock beats Scissors
    # Scissors beats Paper
    # Paper beats Rock
    if roll1 == roll2:
        return None
    elif roll1 == "rock":
        return player1 if roll2 == "scissors" else player2
    elif roll1 == "paper":
        return player1 if roll2 == "rock" else player2
    elif roll1 == "scissors":
        return player1 if roll2 == "paper" else player2

def get_roll(player_name, rolls):
    roll = input(f"{player_name}, enter your roll [rock, paper, scissors]: ")
    roll = roll.lower().strip() # Convert to lowercase to make it case-insensitive
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid play!")
        return None

    return roll

if __name__ == "__main__":
    main()