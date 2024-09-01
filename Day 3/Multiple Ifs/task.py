print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    photos = input("Do you want to take a photo which cost 3$?")
    if photos == "Yes":
        print(f"The total bill is {bill+3}")
    else:
        print(f"The total bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
