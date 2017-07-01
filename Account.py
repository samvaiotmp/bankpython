class Account:
    def __init__(self, name, acno, bal, active):
        self.name = name
        self.acno = acno
        self.bal = bal
        self.active = active

    def isactive(self):
        return self.active

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        self.bal -= amt

    def balance(self):
        return self.bal

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def report(self):
        leng = len(self.name)
        pad = 15 - leng
        padding = str(" "*pad)
        print("name: {}{}  account number: {}     balance:    {}".format(self.name, padding, self.acno, self.bal))