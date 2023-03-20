from random import randint

op_dict = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}


def options():
    print("")
    for key in op_dict:
        print(key, "-", op_dict[key])


def win():
    print("You win!")
    score = 1
    return score


def lose():
    print("You lose!")
    score = 0
    return score


def tie():
    print("It's a tie!")
    score = -1
    return score


def input_check():
    user_input = input("Choose: ")
    if user_input == "" or user_input.lower() == "q":
        return False

    user_input = int(user_input)
    if not 0 < user_input < 4:
        raise Exception

    return user_input


def game(computer, user):
    if computer == user:
        return tie()
    elif computer == 1:
        if user == 2:
            return win()
        else:
            return lose()
    elif computer == 2:
        if user == 1:
            return lose()
        else:
            return win()
    else:
        if user == 1:
            return win()
        else:
            return lose()


def main():
    player_score = 0
    computer_score = 0
    ties = 0

    while True:
        try:
            options()

            computer = randint(1, 3)
            user = input_check()
            if not user:
                break

            print("\nComputer:", op_dict[(computer)])
            print("Player:  ", op_dict[(user)])

            result = game(computer, user)
            if result == 1:
                player_score += 1
            elif result == 0:
                computer_score += 1
            else:
                ties += 1
        except Exception:
            print("\nInvalid choice!")

    print(
        "\nTotal score:\nComputer:",
        computer_score,
        "\nPlayer:  ",
        player_score,
        "\nTies:    ",
        ties,
    )


if __name__ == "__main__":
    main()
