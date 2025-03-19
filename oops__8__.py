#practice question
#create account class with 2 attributes-blance & account no.
#create methods for debit,credit & printing the blance.
class account:
    def __init__(self,blance,acc_no):
        self.blance=blance
        self.acc_no=acc_no
    
    def debit(self,amount):
        self.blance-=amount
        print("$",amount,"was debited")
        print("total blance",self.priting())
    def credit(self,amount):
        self.blance+=amount
        print("$",amount,"was credited")
        print("total blance",self.priting())
    def priting(self):
        return self.blance

acc=account(100000,72)
print(acc.blance)
print(acc.acc_no)
acc.credit(100)
acc.debit(100)
acc.credit(100000)
acc.debit(1)
