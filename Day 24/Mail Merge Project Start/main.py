#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
sample = open("./Input/Letters/starting_letter.txt")
data = sample.read()
with open("./Input/Names/invited_names.txt", "r") as name_list:
    names = name_list.readlines()


for name in names:
    stripped_name = name.strip()
    with open(f"./Output/ReadyToSend/{stripped_name}", "w") as new_letter:
        personalized_letter = data.replace(PLACEHOLDER, stripped_name)
        new_letter.write(personalized_letter)
sample.close()
