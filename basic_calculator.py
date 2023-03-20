# Define the functions needed: add, sub, mul, div
# Print options to the user
# Ask for values
# Call the functions
# While loop to continue the program until the user wants to exit


def add(num1, num2):
    return print("Result:", num1 + num2)


def sub(num1, num2):
    return print("Result:", num1 - num2)


def mul(num1, num2):
    return print("Result:", num1 * num2)


def div(num1, num2):
    return print("Result:", num1 / num2)


operators = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "q": "Quit"
}


def options():
    print("")
    for key in operators:
        print(key, ":", operators[key])
    print("")


if __name__ == "__main__":
    while True:
        try:
            options()
            operator = input("Choose an option: ").lower()
            if operator == "" or operator == "q":
                break
            elif operator not in operators:
                raise Exception

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            if operator == "+":
                add(num1, num2)
            elif operator == "-":
                sub(num1, num2)
            elif operator == "*":
                mul(num1, num2)
            elif operator == "/":
                div(num1, num2)
        except ZeroDivisionError:
            print("Please, don't do weird stuff")
        except Exception:
            print("Invalid")
