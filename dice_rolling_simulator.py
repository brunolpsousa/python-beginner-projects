# Define a function to roll the dice
# Create a dictionary that will have the drawing of the dice

from random import randint

dice_drawing = {
    1: (
        "-----",
        "|   |",
        "| o |",
        "|   |",
        "-----",
    ),
    2: (
        "-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----",
    ),
    3: (
        "-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----",
    ),
    4: (
        "-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----",
    ),
    5: (
        "-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----",
    ),
    6: (
        "-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----",
    ),
}


def roll():
    number = randint(1, 6)
    print("\n" + "\n".join(dice_drawing[number]))


if __name__ == "__main__":
    while True:
        op = input('Roll or quit? ')
        if "q" in op.lower():
            break
        roll()
