class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be greater than zero.")

class SavingsAccount(Account):
    def __init__(self, account_number, minimum_balance):
        super().__init__(account_number)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= self.minimum_balance:
                self.balance -= amount
            else:
                print("Withdrawal amount exceeds minimum balance limit!")
        else:
            print("Withdrawal amount must be greater than zero.")

class ChequingAccount(Account):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
            else:
                print("Withdrawal amount exceeds overdraft limit!")
        else:
            print("Withdrawal amount must be greater than zero.")

class Bank:
    def __init__(self):
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

class Program:
    def __init__(self):
        self.bank = Bank()
    
    def show_main_menu(self):
        while True:
            print("\nBanking Menu:")
            print("1. Open Account ")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                # Bonus: Open Account
                self.open_account()
            elif choice == '2':
                self.show_account_menu()
            elif choice == '3':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    
    def show_account_menu(self):
        account_number = int(input("Enter account number: "))
        account = self.bank.search_account(account_number)
        if account:
            while True:
                print("\nAccount Menu:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit Account")
                choice = input("Enter your choice: ")
                if choice == '1':
                    print("Balance:", account.balance)
                elif choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '4':
                    print("Exiting account menu.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Account not found.")

    def open_account(self):
        account_type = input("Enter account type (Savings/Chequing): ").lower()
        if account_type == 'savings':
            account_number = int(input("Enter account number: "))
            minimum_balance = float(input("Enter minimum balance: "))
            account = SavingsAccount(account_number, minimum_balance)
            self.bank.add_account(account)
            print("Savings account created successfully.")
        elif account_type == 'chequing':
            account_number = int(input("Enter account number: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = ChequingAccount(account_number, overdraft_limit)
            self.bank.add_account(account)
            print("Chequing account created successfully.")
        else:
            print("Invalid account type. Please enter either 'Savings' or 'Chequing'.")

if __name__ == "__main__":
    program = Program()
    program.show_main_menu()
