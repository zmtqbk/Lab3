class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage:

# Create a bank account
account = Account("John Doe", 100)

# Make several deposits and withdrawals
account.deposit(50)  # New balance: 150
account.withdraw(30)  # New balance: 120
account.withdraw(200)  # Insufficient funds
account.deposit(80)  # New balance: 200
account.withdraw(150)  # New balance: 50
account.withdraw(100)  # Insufficient funds
