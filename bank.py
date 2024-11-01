#This comment is for the new assignment "git". If i did any mistakes in doing this assignment tell me in the comments 

class BankAccount:
    def __init__(self, customer_id, name, starting_balance=0.0):
        self.customer_id = customer_id
        self.name = name
        self.balance = starting_balance
        self.transactions = {}  # Dictionary to record transactions

    def print_account_info(self):
        """Prints the account information of the customer."""
        print(f"Customer ID: \033[1m{self.customer_id}\033[0m")
        print(f"Name: {self.name}")
        print(f"Balance: \033[1m${self.balance:.2f}\033[0m")  # From here i bolded every number result for better readability

    def deposit(self, amount):
        """Deposits an amount into the account and records the transaction."""
        if amount > 0:
            self.balance += amount
            self.transactions['deposit'] = self.transactions.get('deposit', 0) + amount
            print(f"Deposited: \033[1m${amount:.2f}\033[0m")  # Bold deposited amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws an amount from the account if sufficient balance exists and records the transaction."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions['withdrawal'] = self.transactions.get('withdrawal', 0) + amount
                print(f"Withdrew: \033[1m${amount:.2f}\033[0m")  # Bold withdrawn amount
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def print_transactions(self):
        """Prints all transactions made by the customer."""
        print("Transactions:")
        for transaction_type, amount in self.transactions.items():
            print(f"{transaction_type}: \033[1m${amount:.2f}\033[0m")  # Bold transaction amounts


# Example usage
if __name__ == "__main__":
    # Example 1
    account1 = BankAccount(customer_id=1, name="John Wick", starting_balance=100.0)
    account1.print_account_info()
    account1.deposit(50)
    account1.withdraw(30)
    account1.withdraw(150)  # Attempt to withdraw more than the balance
    account1.print_transactions()
    account1.print_account_info()
    print("")  # Added a newline for better readability

    # Exmple 2
    account2 = BankAccount(customer_id=2, name="Daisy Beagle", starting_balance=1000.0)
    account2.print_account_info()
    account2.deposit(50)
    account2.withdraw(30)
    account2.withdraw(150)  # Attempt to withdraw more money
    account2.print_transactions()
    account2.print_account_info()
