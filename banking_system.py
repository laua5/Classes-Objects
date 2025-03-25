class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayinfo(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Gender:", self.gender)
        print("Street Address:", self.street_address)
        print("City:", self.city)
        print("Email:", self.email)
        print("cc Number:", self.cc_number)
        print("cc Type:", self.cc_type)
        print("Balance:", self.balance)
        print("Account Number:", self.account_no)
        print("*"*30)


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def findUser():
    user_first = input("Enter the first name of the user: ").title()
    user_last = input("Enter the last name of the user: ").title()
    user_found = False
    for user in userList:
        if user.first_name == user_first and user.last_name == user_last:
            user.displayinfo()
            user_found = True  # User has been found
            break
    if not user_found:
        print("Sorry, no user found with that name.")


def overdrafts():
    print("Users with overdrafts: ")
    for user in userList:
        if user.balance < 0:  # Checks if user has negative balance
            print(f" - {user.first_name} {user.last_name} (${user.balance})")
    overdraft_users = []  # List to store overdraft users
    total_overdraft = 0
    for user in userList:
        if user.balance < 0:  # Checks if user has negative balance
            overdraft_users.append(user)  # Adds users to list
            total_overdraft += user.balance
    print(f"Total users with overdraft accounts is {len(overdraft_users)}")
    print(f"Total amount of users with overdraft is ${total_overdraft:.2f}")


def missingEmails():
    print("Users without emails: ")
    no_email = []
    for user in userList:
        if user.email == "":  # Checks for missing email
            print(f" - {user.first_name} {user.last_name}")
            no_email.append(user)  # Adds users to list
    print(f"Total users with a missing email is {len(no_email)}")


def bankDetails():
    total_balance = 0
    highest_balance = userList[0]  # Assumes first is highest
    lowest_balance = userList[0]  # Assumes first is lowest
    for user in userList:
        total_balance += user.balance
        if user.balance > highest_balance.balance:
            highest_balance = user  # Update if new highest found

        if user.balance < lowest_balance.balance:
            lowest_balance = user  # Update if new lowest found
    print(f"Total number of users is {len(userList)}")
    print(f"Total balance of users is ${total_balance:.2f}")
    print(f"User with the highest balance is {highest_balance.first_name}"
          f" {highest_balance.last_name} with a balance of "
          f"${highest_balance.balance:.2f}")
    print(f"User with the lowest balance is {lowest_balance.first_name}"
          f" {lowest_balance.last_name} with a balance of "
          f"${lowest_balance.balance:.2f}")


def transfer():
    user_account = input("Please enter account number: ")
    sender = None
    for user in userList:
        if user.account_no == user_account:  # Checks if account exists
            sender = user
            break

    if sender is None:
        print("Sorry, no user found with that account number.")
        return
    sender.displayinfo()
    # Get transfer amount
    try:
        amount_transfer = float(input("Amount to transfer: $"))
    except ValueError:
        # Checks if amount entered is not a number
        print("Invalid amount entered. Please enter a numeric value.")
        return
        # Checks if amount entered is negative
    if amount_transfer <= 0:
        print("Transfer amount must be greater than zero.")
        return
        # Checks if amount entered exceeds available balance
    if amount_transfer > sender.balance:
        print("The amount you entered exceeds the available balance.")
        return
    # Get recipient details
    transfer_account = input("Please enter account number to transfer to: ")
    receiver = None
    for user in userList:
        if user.account_no == transfer_account:  # Checks if account exists
            receiver = user
            break
    if receiver is None:
        print("Sorry, no account found with that number.")
        return

    # Confirm transfer
    confirm = input(f"Account number {transfer_account} belongs to "
                    f"{receiver.first_name} {receiver.last_name}. Enter "
                    f"'y' to confirm transfer, or else will be "
                    f"cancelled: ").lower()
    if confirm != 'y':
        print("Transfer canceled.")
        return
    # Updates new balances
    sender.balance -= amount_transfer
    receiver.balance += amount_transfer
    # Confirms successful transaction
    print(f"Transfer successful! ${amount_transfer:.2f} transferred "
          f"from {sender.first_name} {sender.last_name} "
          f"to {receiver.first_name} {receiver.last_name}.")

    # Display updated balances
    print(f"{sender.first_name} {sender.last_name}'s new balance: "
          f"${sender.balance:.2f}")
    print(f"{receiver.first_name} {receiver.last_name}'s new balance: "
          f"${receiver.balance:.2f}")


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()
