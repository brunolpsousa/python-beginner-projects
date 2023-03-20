# Ask user if they want to generate a password or not
# If yes, ask for password lenght
# Generate password
# Print password
# If initial response is no, exit program
from random import choice
import string

initialize_program = str(input("Do you want to generate a password? y/N\n")).lower()
if "y" in initialize_program:
    length = 0
    while not (4 <= length <= 64):
        length = int(input("Enter the password lenght (4 - 64): "))
    data = string.ascii_letters + string.digits + string.punctuation
    result_str = "".join(choice(data) for i in range(length))
    print(result_str)
