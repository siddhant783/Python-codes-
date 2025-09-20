class Amount:
    def _init_(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("Total balance ",self.getbalance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was debited")
        print("total balance",self.getbalance())
    def getbalance(self):
        return self.balance
acc1=Amount(1000,12345)
acc1.credit(400)
acc1.debit(800)