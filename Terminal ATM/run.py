# Main ATM Program
from atm_user import user

# Function TO Prompt The User To Login


def login():
    print("==== ATM Login ====")
    username = input("Enter Your User ID: ")
    if username in user_logins:
        password = input("Enter your password: ")
        if user_logins[username].UserPin == password:
            print(f"Welcome, {username}!")
            return user_logins[username]
        else:
            print(f"That Was The Wrong Password")
            return None
    else:
        print(f"That Was The Wrong User ID")
        return None

    # You can add validation here for the username and password


# Function To Display ATM Menu That Takes A User As An Argument. User That Logged In Will Be Passed As Argument


def atm_menu(user):
    run = True
    while run:
        menu = """
        ==== ATM Menu ====
        1. Deposit
        2. Withdraw
        3. View Balance
        4. View Transaction History
        5. Exit

        Please select an option (1-5): 
        """
        choice = input(menu)

        if choice == '1':
            deposit = int(input("Enter How Much You Would Like To Deposit :"))
            user.deposit(deposit)
        elif choice == '2':
            withdraw = int(
                input("Enter How Much You Would Like To Withdraw : "))
            user.withdraw(withdraw)
        elif choice == '3':
            user.check_balance()
        elif choice == '4':
            user.view_transaction_history()
        elif choice == '5':
            run = False
        else:
            print("Invalid option, please try again.")


# Test User Login Information. You Would Want To Save This In A Seperate File And Encrypt The Information
# In Future When Implementing GUI Add Code For More Improved User Creation Functionality
user_logins = {
    "1111": user("1111", "1111"),
    "2222": user("2222", "2222"),
    "3333": user("3333", "3333")
}

# Main Program
user = login()
if user != None:
    atm_menu(user)
