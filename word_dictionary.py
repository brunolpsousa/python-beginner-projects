# Have a python dictionary that has a key/value pair that represents a word and
# it's definition
# Collect input from the user, input a word
# Check if the word is in the dictionary
# Print definition

word_dictionary = {
    "hi": "a way of greeting",
    "eyes": "an organ for seeing",
    "earth": "a planet in space",
}


def main2():
    while True:
        try:
            word = input("\nType a word: ").lower()
            if word == "" or word == "q":
                break
            elif word in word_dictionary:
                print("Definition:", word_dictionary[word])
            else:
                print(f'No definitions matches for "{word}"')
        except Exception as e:
            print(e)


def main():
    while True:
        try:
            word = input('\nType a word: ').lower()
            if word == "" or word == "q":
                break
            word_found = None
            for key in word_dictionary:
                if word == key:
                    word_found = True
                    print("Definition:", word_dictionary[word])
            if not word_found:
                print(f'No definition matches for "{word}"')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
