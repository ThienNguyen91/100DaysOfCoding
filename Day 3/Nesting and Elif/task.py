print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("How old are you? "))
    if age > 18:
        print("It's will be 12$")
    elif age < 12:
        print("It's will be 5$")
    else:
        print("It's will be 7$")
else:
    print("Sorry you have to grow taller before you can ride.")
