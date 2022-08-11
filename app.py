'''
Workshop 3 framework v1.1
By Jack Seymour

# Follow allong with the written workshop instructions and
    use this application stub to impliment the functionality.

# Locations marked with TODO: are places that need implimentation.

# The pass command in a stub is used to end a block and continue execution.
    This is used to define portsion of code structure that are awaiting implimentation.
    You should remove pass when you impliment the functionality.
'''
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

# Main application loop
while True:
    show_homepage(authorized_user)

    choice = input("Chose an option: ")

    if choice == "1":
        username = input("\nEnter username: ").lower()
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif choice == "2":
        username = input("\nEnter username: ").lower()
        password = input("Enter password: ")
        authorized_user = register(database, username, password)

        if authorized_user != "":
            database[authorized_user] = password

    elif choice == "3":

        if authorized_user == "":
            print("\nYou are not logged in!")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif choice == "4":
        show_donations(donations)

    elif choice == "5":
        print("\nGoodbye!")
        break
