height = float(input())

try:
    if height >3:
        raise ValueError("Too high")
except ValueError:
    print(f"Human not should be taller than {3} metter")
