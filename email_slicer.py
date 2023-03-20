# Collect email from user
# Split the email using the @, the first part as the user name, the second part
# is gonna be saved as domain
# Split domain using .,


def extensions(extension):
    ext = ""
    for i in extension:
        ext += i + " "
    return ext


def main2():
    try:
        email = input("Enter an email: ").split("@")

        username = email[0]
        domain = email[1].split(".")
        extension = domain[1:]

        print(
            "Username = " + username + "\nDomain = " + domain[0],
            "\nExtension =",
            extensions(extension),
        )
    except Exception as e:
        print(e)


def main():
    email_input = input("Input your email adress: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)


main2()
