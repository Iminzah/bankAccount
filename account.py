class BankAccount:
    bank = "KCB"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))

    def withdraw(self, amount):
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You don't have enough balance")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))


    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)
