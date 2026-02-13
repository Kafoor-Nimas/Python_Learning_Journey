class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
            if amount >0:
                self.balance +=amount
                print(f"{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")

    def withdraw(self,amount):
            if amount <= self.balance:
                self.balance -=amount
                print(f"{amount} withdrawn successfully")
            else:
                print("Insufficient funds.")

    def check_balance(self):
            print(f"Account Holder: {self.account_holder}")
            print(f"Current balance: {self.balance}")

#testing the class
acc1 =BankAccount("John")
acc2 =BankAccount("Anna",500)

acc1.deposit(1000)
acc1.withdraw(300)
acc1.check_balance()

print("----------")

acc2.withdraw(200)
acc2.deposit(400)
acc2.check_balance()