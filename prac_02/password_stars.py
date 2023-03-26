LENGTH_LIMIT = 5

def main():
    password = get_password()
    print("*" * len(password))

def get_password():
    custom = input(str("Password:"))
    while len(custom) <= LENGTH_LIMIT:
        print("Password of at least five characters.")
        custom = input(str("Password:"))
    else:
        return custom

main()
