from datetime import datetime


class Account:


    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan_amount = 0
        self.loan_repayment=[]





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
            time=datetime.now()
            deposit={
                "time":time,
                "amount":amount
            }
            self.deposits.append(deposit)
            formatted_time=time.strftime("%A,%drd %B %Y,%H:%M %p")
            print("You deposited {} to {} on {}".format(amount,self.account_name(), formatted_time
            )
            )
    def show_deposit_statement(self):
        for deposit in self.deposits:
            time=deposit['time']
            formatted_time=self.get_formatted_time(time)
            amount=deposit['amount']
            statement="You deposited {} on {}".format(amount,formatted_time)
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
            time=datetime.now()
        withdraw={
                "time":time,
                "amount":amount
            }
        self.withdrawals.append(withdraw)
        formatted_time=time.strftime("%A,%drd %B %Y,%H:%M %p")
        print("You withdrawn {} from {} on {}".format(amount,self.account_name(), formatted_time))
               
            
            
    def  get_withdrawal_statement(self):
       for withdraw in self.withdrawals:
            time=withdraw['time']
            formatted_time=self.get_formatted_time(time)
            amount=withdraw['amount']
            statement="You withdrew {} on {}".format(amount,formatted_time)
            print(statement)

    def get_balance(self):
        return "The balance for {} is {}".format(
            self.account_name(), self.balance
        )
    def get_formatted_time(self,time):
        return time.strftime("%A, %drd %B %Y, %H:%M %p")

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
            time=datetime.now()
            repayment={
                'time':time,
                'amount':amount
            }
            self.loan_repayment.append(repayment)
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
    def loan_repayment_statement(self):
        for repayment in self.loan_repayment:
            time=repayment['time']
            amount=repayment['amount']
            formatted_time=self.get_formatted_time(time)
            statement="You repaid {} on {}".format(amount, formatted_time)
            print(statement)
class BankAccount(Account):
    def __init__(self, first_name,last_name,phone_number,bank):
        self.bank=bank
        super().__init__(self,first_name,last_name,phone_number)

class MobileMoneyAccount(Account):
    def __init__(self, first_name,last_name,phone_number,service_provider):
        self.service_provider=service_provider
        self.airtime=[]
        self.received=[]
        self.sent=[]
        self.bill=[]
        super().__init__(self,first_name,last_name,phone_number)

    def buyAirtime(self,amount):
        try:
            amount+1
        except TypeError:
            print("Please put amount in figures")
            return
        if self.balance < amount:
            print("You do not have enough. Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            airtime={
                "time":time,
                "airtime":amount
            }
        self.airtime.append(airtime)
        print("You have bought airtime of ksh {} at {}".format(amount,self.get_formatted_time(time)))

    def sendMoney(self,amount):
        try:
            amount+1
        except TypeError:
            print("Please enter amount in figures")
            return
        if self.balance< amount:
            print("You do not have sufficient balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            sent={
                "time":time,
                "sent":amount
            }
        self.sent.append(sent)
        print("You have sent ksh {} at {}".format(amount,self.get_formatted_time(time)))

    def receiveMoney(self,amount):
        self.balance+=amount
        time=datetime.now()
        receive={
            "time":time,
            "received":amount
        }
    self.receive.append(receive)
    print("You have received ksh{} at {}.Your balance is {}".format(amount,self.get_formatted_time(time)),self.balance)
   
   
     def pay_bill(self,amount):
        try:
            amount+1
        except TypeError:
            print("Please enter amount in figures")
        if self.balance < amount:
            print("You do not have enough money.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            bill={
                "time":time,
                "bill":amount
            }
        self.bill.append(bill)
        print("You have paid a bill of {} at {}".format(amount,self.get_formatted_time(time)))