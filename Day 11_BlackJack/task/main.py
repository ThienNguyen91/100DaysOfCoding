import Blackjack

while True:
    ask_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_play.lower() == "y":
        # run program
        Blackjack.blackjack_game()
    elif ask_play.lower() == "n":
        break
