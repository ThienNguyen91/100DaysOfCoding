#TODO: Create a letter using starting_letter.txt
#constant
import os.path

PLACEHOLDER = "[name]"
INPUT_NAMES_FILE = "./Input/Names/invited_names.txt"
INPUT_LETTER_FILE = "./Input/Letters/starting_letter.txt"
OUTPUT_DIR = "./Output/ReadyToSend/"


if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

#Read data from sample letter
with open(INPUT_LETTER_FILE) as sample:
    data = sample.read()

#read all names
with open(INPUT_NAMES_FILE) as name_list:
    names = name_list.readlines()

#Create personalized letters
for name in names:
    name = name.strip()
    personalized_letter = data.replace(PLACEHOLDER, name)

    output_file = os.path.join(OUTPUT_DIR, f"{name}.txt")
    with open(output_file, "w") as new_letter:
        new_letter.write(personalized_letter)