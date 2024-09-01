db = {}
import art
print(art.logo)
print("Welcome to the secret auction program")
while True:
    name = input("What is your name?: ")
    bid_amount = input("What is your bid?: ")
    db[name] = int(bid_amount)
    ask_for_other = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if ask_for_other.lower() == "no":
        break
largest = 0
count = 1
winner = ""
for name in db:
    if db[name] > largest:
        largest = db[name]
        winner = name
        count = 0
    if db[name] >= largest:
        count += 1

if count == 1:
    print(f"The winner is {winner} with a bid of a ${largest}")

else: #same bid
    print("There is a tie between the following bidders: ", end = "")
    list_user = {}  # Dictionary to store users with the tied bid

    for name in db:
        if db[name] == largest:
            list_user[name] = 0
            print(f"{name} ", end="")

    for name in list_user:
        new_bid = int(input(f"\nHow many bid for {name}? "))
        list_user[name] = new_bid


    largest = 0
    for name in list_user:
        if list_user[name] > largest:
            largest = list_user[name]
            winner = name
    print(f"Winner is {winner} with ${largest}")


