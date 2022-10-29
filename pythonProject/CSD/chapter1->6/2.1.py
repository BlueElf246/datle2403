class CreditCard:
    def __init__(self,customer,bank,acnt,limit):
        self._customer=customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
         return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
         return self._balance
    def charge(self,price):
        if price+self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
    def _set_balance(self,price):
        self._balance+=price
    def make_payment(self,price):
        self._balance-=price
class PredatoryCreditCard(CreditCard):
    def __init__(self,customer, bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)
        self._apr=apr
    def charge(self,price):
        if super().charge(price) == False:
            self._balance+=5
    def process_month(self):
        if self._balance >0:
            monthly_factor=pow(1+self._apr,1/12)
            super()._set_balance(monthly_factor)












# if __name__ == '__main__':
#     wallet = [ ]
#     wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,'5391 0375 9387 5309' , 2500) )
#     wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500) )
#     wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000) )
#     for val in range(1, 17):
#         wallet[0].charge(val)
#         wallet[1].charge(2 *val)
#         wallet[2].charge(3 *val)
#     for c in range(3):
#         print( 'Customer =' , wallet[c].get_customer())
#         print( 'Bank =' , wallet[c].get_bank())
#         print( 'Account =' , wallet[c].get_account())
#         print( 'Limit =' , wallet[c].get_limit())
#         print( 'Balance =', wallet[c].get_balance())
#         while wallet[c].get_balance( ) > 100:
#             wallet[c].make_payment(100)
#             print( 'New balance = ', wallet[c].get_balance())
#         print( )
