from Account import Account

class Checking(Account):
    def __init__(self,name,acno,bal,active,fees):
        Account.__init__(self, name,acno,bal,active)
        self.fees = fees

    def surcharge(self):
        return self.fees

    def deposit(self, amt):
        self.bal = Account.deposit(amt)
        self.bal -= self.fees

    def withdraw(self, amt):
        self.bal = Account.withdraw(amt)
        self.bal -= self.fees