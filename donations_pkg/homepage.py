'''
Homepage functions
'''
def show_homepage(authorized_user):
    '''
    show_homepage
    '''
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")    
    if authorized_user == "":
        print("\nYou Must be logged in to donate.")
    else:
        print("logged in as: ", authorized_user)
    print("")

def donate(username):
    '''
    donate
    '''
    donation_amt = float(input("\nEnter amount to donate: "))
    donation = username + " donated $" + str(donation_amt)
    print("Thank you for your donation!")
    print("")
    return donation

def show_donations(donations):
    '''
    show_definition
    '''
    if len(donations) == 0:
        print("\n--- All Donations ---")
        print("Currently, there are not donations.")
        print("")
    else:
        total = 0
        for donation in donations:
            print(donation)
            idx = donation.find("$") + 1
            total += float(donation[idx:])
        print("Total = $" + str(total))
        print("")
