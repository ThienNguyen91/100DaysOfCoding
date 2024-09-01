import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operator_list = {"+": add, "-": subtract, "*": multiply, "/": divide}

def caculator(num):

    operator = input("""
    +
    -
    *
    /
    Pick an operation:""")
    num2 = int(input("What's the next number?: "))
    result = 0
    if operator not in operator_list or type(num) != int or type(num2) != int:
        print(f"Wrong type")
    else:
        result = operator_list[operator](num, num2)
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if again.lower() == "y":
        caculator(result)
    return result

print(art.logo)
num = int(input("What's the first number?: "))
caculator(num)



