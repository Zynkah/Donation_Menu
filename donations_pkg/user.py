
'''
User functions
'''
def login(database, username, password):
    '''
    login
    '''
    if username.lower() in database:
        if password == database[username]:
            print("\nWelcome back", username + "!")
            print("")
            return username
        if password != database[username]:
            print("\nIncorrect password for", username + "!")
            print("")
            return ""

    print("\nUser not found. Please register.")
    return ""


def register(database, username, password):
    '''
    register
    '''
    if username.lower() in database:
        print("\nUsername already registered!")
        print("")
        return ""
    if len(username) > 10:
        print("\nUsername must be less than 10 characters")
        print("")
        return ""
    if len(password) <= 5:
        print("\nPassword must be more than 5 characters")
        print("")
        return ""

    print("\nUsername ", username, "registered!")
    print("")
    return username.lower()
