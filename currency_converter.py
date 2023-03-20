def convert_to_dollar(real):
    return real / 5.27


def main():
    try:
        real = eval(input("Enter amount in BRL: RS "))
        dollar = convert_to_dollar(real)
        print("That is $%.2f" % dollar)
    except Exception:
        print("Not a valid value\n")
        main()


if __name__ == "__main__":
    main()
