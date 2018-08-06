class Account:
    """Docstring for Accounts"""
    type="savings"
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class checking(Account):
    """Docstring for Accounts"""
    type="checking"
    def __init__(self,filepath,fee):
        self.fee=fee
        Account.__init__(self,filepath)

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee



check=checking("balance.txt",44)
check.transfer(20)
print(check.balance)
check.commit()
print(check.type, check.__doc__)
