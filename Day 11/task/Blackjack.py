cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art
import random

def blackjack_game():
    print(art.logo)
    player_card = [random.choice(cards), random.choice(cards)]
    computer_card = [random.choice(cards)]
    current_card(player_card, computer_card)
    if sum(player_card) <= 21:
        player_card = askToDraw(player_card,computer_card)

# If player have ace and the total number exceed 21
    while 11 in player_card and sum(player_card) > 21:
        player_card = ace_case(player_card, computer_card)

    if sum(player_card) > 21:
        final(player_card, computer_card)
    else: #computer draw card
        while sum(computer_card) < 17:
            computer_card.append(random.choice(cards))
        final(player_card, computer_card)
def askToDraw(player_card,computer_card):
    """Draw until player stop or exceed 21"""
    while sum(player_card) <= 21:
        ask_to_draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask_to_draw not in ["y", "n"]:
            print("Invalid input. Please type 'y' or 'n'.")
            continue
        elif ask_to_draw == "y":
            random_card = random.choice(cards) # draw 1 card
            ## the card is ace but 11 will exceed 21
            if random_card == 11 and sum(player_card) + 11 > 21: # player have ace card but add 11 will exceed 21
                player_card.append(1)
            else:
                player_card.append(random_card)
            current_card(player_card,computer_card)
        elif ask_to_draw == "n":
            break
    return player_card

def final(player_card, computer_card):
    total_player = sum(player_card)
    total_computer = sum(computer_card)
    print(f"Your final hand: {player_card}, final score: {total_player}")
    print(f"Your final hand: {computer_card}, final score: {total_computer}")

    if total_player > 21 and total_computer > 21 or total_player == total_computer > 21:
        print("You draw")
    elif total_player > 21:
        print("You went over. You lose 😭")
    elif total_computer > 21:
        print("You win.")
    elif total_player < total_computer:
        print("You went over. You lose 😭")
    else:
        print("You win.")


#If player have ace and the total number exceed 21
def ace_case(player_card, computer_card):
    player_card[player_card.index(11)]  = 1

    if sum(player_card) > 21:
        return player_card

    elif sum(player_card) <= 21:
        player_card = askToDraw(player_card, computer_card)
    return player_card
def current_card(player_card, computer_card):
    print(f"Your cards: {player_card}, current score: {sum(player_card)}")
    print(f"Computer's first card: {computer_card[0]}")