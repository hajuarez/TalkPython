import random

def main():
    show_header()

    player = "You"
    ai = "Computer"

    play_game(player, ai)

def show_header():
    print("--------------------------------")
    print("Rock Paper Scissors v1")
    print("--------------------------------")

def play_game(player_1, player_2):
    rolls = ["rock", "paper", "scissors"]

    roll1 = get_roll(player_1, rolls)
    roll2 = random.choice(rolls)                #2nd player automated, no need to validate input

    if roll1 is None:
        print("Can't play that, exiting!")
        return

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

def get_roll(player_name, rolls):
    roll = input(f"{player_name}, enter your roll [rock, paper, scissors]: ")
    roll = roll.lower().strip() # Convert to lowercase to make it case-insensitive
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid play!")
        return None

    return roll

if __name__ == "__main__":
    main()