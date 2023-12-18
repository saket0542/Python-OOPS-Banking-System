class User:
    def __init__(self,name,age,account_no):
        self.name=name
        self.age=age
        self.account_no=account_no

    def show_details(self):
        print(f"User name is {self.name}, age is {self.age} and Account No is {self.account_no}")



class Bank(User):
    def __init__(self,name,age,account_no,balance):
        super().__init__(name,age,account_no)
        self.balance=0

    def show_details(self):
        super().show_details()

    def view_balance(self):
        print(f"Your current Bank Balance is {self.balance}Rs")

    def deposit_money(self,money):
        self.balance=self.balance+money
        print(f"Money Deposited Successfully")

    def withdrawl(self,amount):
        if amount>self.balance:
            print("Insufficent Bank Balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawl Successfull")


User1=Bank("saket",25,434646365364,0)
User1.show_details()
User1.deposit_money(100000)
User1.view_balance()
User1.withdrawl(20000)
User1.view_balance()






