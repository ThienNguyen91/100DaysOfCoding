import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while difficulty not in ['easy', 'hard']:
    print("Something went wrong, please write again.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)
attempt = {"easy": 10, "hard": 5}
player_attempt = attempt[difficulty]
while player_attempt > 0:
    print(f"You have {player_attempt} attempts remaining to guess the number.")
    Number_guess = int(input("Make a guess: "))
    if Number_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
    elif Number_guess > random_number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
    player_attempt -= 1
if player_attempt == 0:
    print("You've run out of guesses, you lose.")


