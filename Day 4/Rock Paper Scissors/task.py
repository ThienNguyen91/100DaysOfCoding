import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Order = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player_choose < 0 or player_choose >= len(Order):
    print("Invalid choice. You must choose 0, 1, or 2.")
else:
    computer_choose = random.randint(0, len(Order)-1)
    print("Player: \n" + Order[player_choose])
    print("Computer: \n" + Order[computer_choose])
    if player_choose == computer_choose:
        print("draw")
    elif ((player_choose == 0 and computer_choose == 2) or
          (player_choose == 1 and computer_choose == 0) or
          player_choose == 2 and computer_choose == 1):
        print("Player wins")
    else:
        print("Computer wins")


