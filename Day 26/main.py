import pandas

INPUT_DIR = "nato_phonetic_alphabet.csv"

#TODO 1. Create a dictionary in this format:
with open(INPUT_DIR) as file:
    DATA = pandas.read_csv(file)
ALPHABET = {row.letter: row.code for index, row in DATA.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type something here: ")
word_list = [ALPHABET[word.upper()] for word in user_input]
print(word_list)
