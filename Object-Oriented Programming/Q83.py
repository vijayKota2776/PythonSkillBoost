class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrawal of ${amount:.2f} successful."
            else:
                return "Insufficient funds. Cannot withdraw."
        else:
            return "Withdrawal amount must be greater than 0."

    def check_balance(self):
        return self.balance
account_holder = input("Enter account holder's name: ")
initial_balance = float(input("Enter the initial balance (default 0): "))
account = BankAccount(account_holder, initial_balance)
while True:
    print("\nBank Account Operations:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Select an operation: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount))
    elif choice == 3:
        print(f"Current balance: ${account.check_balance():.2f}")
    elif choice == 4:
        print("Exiting the bank account system.")
        break
    else:
        print("Invalid option. Please try again.")