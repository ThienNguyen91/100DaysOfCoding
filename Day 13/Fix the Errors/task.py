age = 0
while True:
    try:
        age = int(input("How old are you?"))
        break
    except ValueError:
        print("Wrong input")
if age > 18:
    print(f"You can drive at age {age}.")
