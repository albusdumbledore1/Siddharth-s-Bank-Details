class Bank:
    def __init__(self,accNo,acctype,balance,name):
        self.name=name
        self.accNo=accNo
        self.acctype=acctype
        self.balance=balance

    def balanceEnquiry(self):
        print("your balance is : ", self.balance)

    def withdrawal(self,amount):
        self.balance=self.balance-amount
        print("withdrawal successful, your new balance is : ",self.balance)
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("deposit successful, your new balance is : ",self.balance)

siddharth=Bank('5112007','savings',20000000,'Siddharth')
siddharth.balanceEnquiry()
siddharth.withdrawal(9000000)
siddharth.deposit(10000000)


