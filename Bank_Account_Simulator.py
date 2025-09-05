# Bank Account Simulator

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    """Main function."""
    account = BankAccount()
    while True:
        print("\nBank Account Simulator:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()