import random

print("--------------------------------------------")
print("     M&M guessing game!")
print("--------------------------------------------")

print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = 79#random.randint(1, 100)
attempt_limit = 8
attempts = 0

while attempts < attempt_limit:
    guess = int(input("How many M&Ms are in the jar? "))
    attempts += 1

    if guess == mm_count:
        print("Congratulations! You guessed the correct number of M&Ms!")
        break
    elif guess < mm_count:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    

print("Number of M&Ms in the jar: ", mm_count)
print(f"Bye, you had {attempts} attempts!")    
