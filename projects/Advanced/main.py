# FIXME: add shared logger and
"""
Logger should output messages to both the console and a file
log menu choices
log errors with stack
log start and end of main
"""


def print_menu():
    print(
        """
    1. Print hello world
    2. Create an error
    3. Exit
    """
    )


def main():

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello World")
        elif choice == "2":
            print(1 / 0)
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
