# create account class with 2 attributes - balance & account no
# create methods for credit , debit and printing the balance


class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("rs.", amount, "was debited")
        print("total amount= ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("rs.", amount, "was credited")
        print("total amount= ", self.get_balance())

    def get_balance(self):
        return self.balance


account1 = Account(10000, 9876554321)
account1.debit(1000)
account1.credit(500)
account1.credit(40000)
