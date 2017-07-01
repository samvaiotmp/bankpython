from Account import Account
from Checking import Checking

shaf = Account("Shaf",1001, 100.00, True)
ilm = Account("Ilm", 1002, 200.00, True)
sonu = Account("Sonu", 1003, 150.00, True)

shaf.deposit(20.00)
ilm.deposit(10.00)
sonu.withdraw(25.00)

shaf.report()
ilm.report()
sonu.report()

shaf.deactivate()
shaf.report()

a = Checking("Adam", 2001, 200.00, True, 1.50)
b = Checking("Beth", 2002, 150.00, True, 2.00)

a.deposit(10.00)
b.deposit(100.00)

a.report()
b.report()

b.withdraw(20.00)
b.report()

x = Checking("Xray", 3001, 200.00, True, 1.00)
y = Checking("Yak", 3002, 250.00, True, 2.00)

x.deposit(10.00)
y.deposit(100.00)

x.report()
y.report()

x.withdraw(20)
x.report()