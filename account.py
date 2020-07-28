from datetime import datetime


class BankAccount:


    def __init__(self, first_name, last_name, bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan_amount = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name
        )
        return name

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter amount in figures.")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            date = datetime.now().strftime("%d %B, %Y")
            time = datetime.now().strftime("%H:%M:%S")
            statement = "On {} at {}, Ksh {} was deposited into {}".format(
                date, time, amount, self.account_name()
            )
            self.deposits.append(statement)
            print("Dear {} you have deposited {} at {} on {}.Your new balance is {}".format(self.account_name(),amount,time,date,self.balance)
               
            )
        
    def get_deposit_statement(self):
        for statement in self.deposits:
            print(statement)

    def withdraw(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter amount in figures.")
            return

        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You don't have enough balance")
        else:
            self.balance -= amount
            date=datetime.now().strftime("%d %B,%Y")
            time= datetime.now().strftime("%H:%M:%S")
            statement="On {} at {}, ksh {} withdrawn from {}".format(date,time,amount,self.account_name())
            self.withdrawals.append(statement)
            print(
                "You have withdrawn {} from {}".format(
                  amount, self.account_name()
                )
                
            )
            
    def  get_withdrawal_statement(self):
       for statement in self.withdrawals:
         print(statement)

    def get_balance(self):
        return "The balance for {} is {}".format(
            self.account_name(), self.balance
        )

    def get_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter amount in figures.")
            return

        
        if amount <= 0:
            print("You cannot borrow 0 or a negative value")
        else:
            self.loan_amount += amount
            self.balance += amount
            print(
                "A loan of Ksh {} has been successfully deposited into {}. Your new account balance is {}".format(
                    amount, self.account_name(), self.balance
                )
            )

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter amount in figures.")
            return

        if self.loan_amount == 0:
            print(
                "There is no pending loan for {}".format(self.account_name())
            )
        elif amount <= 0:
            print("You cannot repay 0 or a negative value")
        elif self.balance < amount:
            print(
                "You do not have enough balance to repay that amount of your loan"
            )
        elif self.loan_amount < amount:
            loan = self.loan_amount
            extra = amount - loan
            self.balance -= self.loan_amount
            self.loan_amount = 0
            print(
                "You have successfully completed repaying your loan of Ksh {}. The extra Ksh {} has been retained in your account".format(
                    loan, extra
                )
            )
        else:
            self.balance -= amount
            self.loan_amount -= amount
            if self.loan_amount > 0:
                print(
                    "You have successfully repaid Ksh {} of your loan. Your pending loan balance is Ksh {}".format(
                        amount, self.loan_amount
                    )
                )
            if self.loan_amount == 0:
                print(
                    "You have successfully completed repaying your loan of Ksh {}".format(
                        amount
                    )
                )

acc1=BankAccount("sharon","prudence","equity","5777899")
acc1.deposit(678)
acc1.deposit(567898)
acc1.get_deposit_statement()
acc1.get_loan(346)
acc1.repay_loan(45)
acc1.withdraw(24)
acc1.get_withdrawal_statement()
          