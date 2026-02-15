class BankAccount:
    total_accounts = 0

    def __init__(self, holder_name):
        self.holder_name = holder_name
        BankAccount.total_accounts += 1
        self.__account_number = BankAccount.total_accounts
        self.__balance = 0.0

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.__balance < amount:
            print("Transaction denied")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


class SavingsAccount(BankAccount):
    def __init__(self, holder_name, interest_rate=0.05):
        super().__init__(holder_name)
        self.__interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)


class VIPAccount(BankAccount):
    def __init__(self, holder_name, overdraft_limit=-1000.0):
        super().__init__(holder_name)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        projected_balance = self.get_balance() - amount
        if projected_balance < self.__overdraft_limit:
            print("Transaction denied")
            return
        self.__balance = projected_balance  # Direct internal update


# Test code (remove for submission)
if __name__ == "__main__":
    acc1 = BankAccount("Alice")
    acc1.deposit(1000)
    acc1.withdraw(500)
    print(f"Account 1 balance: {acc1.get_balance()}")
    print(f"Total accounts: {BankAccount.total_accounts}")

    savings = SavingsAccount("Bob", 0.05)
    savings.deposit(1000)
    savings.apply_interest()
    print(f"Savings balance: {savings.get_balance()}")

    vip = VIPAccount("Charlie")
    vip.deposit(500)
    vip.withdraw(800)
    print(f"VIP balance: {vip.get_balance()}")