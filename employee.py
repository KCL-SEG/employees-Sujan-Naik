"""Employee pay calculator."""
from abc import ABC, abstractmethod
from enum import Enum

"""ENTER YOUR SOLUTION HERE!"""

class Contract(ABC):
    @abstractmethod
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Dynamic:

    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate
        self.pay = amount * rate

class HourlyContract(Contract, Dynamic):
    def __init__(self, hours, rate):
        super().__init__(hours,rate)

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f'contract of {self.amount} hours at {self.rate}/hour.'

class VariableCommission(Contract, Dynamic):
    def __init__(self, contracts, rate):
        super().__init__(contracts,rate)

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f'receives a commission for {self.amount} contract(s) at {self.rate}/contract hours.'

class FixedContract(Contract):
    def __init__(self, pay):
        self.pay = pay

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f'works on a monthly salary of {self.pay}.'


class FixedCommission(Contract):
    def __init__(self, pay):
        self.pay = pay

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f'receives a bonus commission of {self.pay}.'


class Employee:

    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        if commission is not None:
            self.has_commission = True
            self.commission = commission
        else:
            self.has_commission = False


    def get_pay(self):
        if self.has_commission:
            return self.commission.get_pay() + self.contract.get_pay()
        else:
            return self.contract.get_pay()

    def __str__(self):
        if self.has_commission:
            return f'{self.name} {str(self.contract)} and {str(self.commission)} Their total pay is {self.get_pay()}.'
        else:
            return f'{self.name} {str(self.contract)}. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', FixedContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',HourlyContract(100,25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', FixedContract(3000), VariableCommission(4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150,25), VariableCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', FixedContract(2000), FixedCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120,30), FixedCommission(600))
