import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
count = len(chosen_word)
corrected_word = []
while count > 0:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrected_word.append(letter)
            count -= 1
        elif letter in corrected_word:
            display += letter
        else:
            display += "_"

    print(display)
print("You won")
