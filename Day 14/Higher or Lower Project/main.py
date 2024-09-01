import art
import game_data
import random
print(art.logo)
player_score = 0
def check_answer(player_choose, character_A, character_B):
    if player_choose.upper() not in ["A", "B"]:
        return False
    elif character_A["follower_count"] < character_B["follower_count"]:
        return player_choose.upper() == "B"
    else:
        return player_choose.upper() == "A"
def Start(Score):
    character_A = random.choice(game_data.data)
    character_B = random.choice(game_data.data)
    while True:
        while character_A == character_B:
            character_B = random.choice(game_data.data)

        print(f"Compare A: {character_A['name']}, a {character_A['description']}, from {character_A['country']}.")
        print(art.vs)
        print(f"Against B: {character_B['name']}, a {character_B['description']}, from {character_B['country']}.")
        player_choose = input("Who has more followers? Type 'A' or 'B': ")
        result = check_answer(player_choose, character_A, character_B)
        if not result:
            print(f"Sorry, that's wrong. Final score: {Score}")
            break
        else:
            Score += 1
            print(f"You're right! Current score: {Score}.")
            character_A = character_B
            character_B = random.choice(game_data.data)




Start(player_score)