class BankAccount:

    __balance = 0

    def __init__(self):
        self.__balance = 0

    def deposit(self, money_in):
        self.__balance = self.__balance + money_in
        return self.__balance

    def withdraw(self, remove_money):
        self.__balance = self.__balance - remove_money
        return self.__balance

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):

    interest_rate = 0.04
    newBal = 0

    def add_interest(self):
        self.newBal = SavingsAccount.get_balance(self) * (1 + self.interest_rate)
        print(self.newBal)
        return self.newBal


bankAcc1 = SavingsAccount()
bankAcc1.deposit(43000)
bankAcc1.withdraw(237)
bankAcc1.get_balance()

bankAcc1.add_interest()

