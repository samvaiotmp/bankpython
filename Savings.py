from Account import Account

class Saving(Account):
    def __init__(self,name,acno,bal,active,interest):
        Account.__init__(self, name,acno,bal,active)
        self.interest = interest

    def rate(self):
        return self.interest

    def deposit(self, amt):
        self.bal = Account.deposit(amt)
        self.bal = self.bal + (amt * self.interest / 100)

    def withdraw(self, amt):
        print("Withdrawl not allowed from savings account")