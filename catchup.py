#OOP
 #CLASS
 #INSTANCE
 #CLASS ATTRIBUTES 
 #instance attributes and methods
 #inheritance
 #decorator

class Bank_accounts:
    total_balance = 0

    def __init__(self, acc_number, acc_name, balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance
        Bank_accounts.total_balance += balance

    def deposit(self, amount):
        self.balance += amount
        Bank_accounts.total_balance += amount

    @classmethod

    def total_bank_balance(cls):
        print(cls.total_balance)

    def deposit(self, amount):
        self.balance += amount


    def check_balance(self):
        print(f"Hello {self.acc_name}, your current balance is {self.balance}")

    def withdraw(self, amount):
        if  amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Hello {self.acc_name}, you have successfully withdrawn ksh{amount}, your current balance is {self.balance}")

        else:
            print("Insufficient balance")

class SavingsAccount(Bank_accounts):
    def add_interest(self):
        self.balance *= 1.03
    



Bin = Bank_accounts(1222222, "Bin Amin", 0)
Derrick = Bank_accounts(1222222,"Derrick", 5000)            
Derrick.deposit(15000)
Bin.deposit(10000)
print(Bin.balance)
print(Derrick.balance)
print(Derrick.check_balance())
print(Derrick.withdraw(2000))
Bin.deposit(60000)

print(Bank_accounts.total_balance)