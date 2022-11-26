#!/usr/bin/env python3

class CreditCard:
    """ A basic Credit Card example class"""

    def __init__(self, customer, bank, accnt, limit):
        """ Creates a new credit card instance.

        Initial balance is 0.

        customer: name of the customer (e.x. 'John Doe')
        bank:     name of the bank (e.x. 'Chase')
        accnt:    account identifier (e.g. '1234 5678 90')
        limit:    credit limit (in USD)
        """
        self._customer = customer
        self._bank     = bank
        self._account  = accnt
        self._limit    = limit
        self._balance  = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return bank's name"""
        return self._bank

    def get_account(self):
        """Return the CC #"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current CC balance"""
        return self._balance

    def charge(self, price):
        """Charge to account balance 'price' amount, assuming sufficient credit
        limit.

        Returns True if charge was processed, False if charge was declined due
        to insufficient credit.
        """
        if price + self._balance > self._limit:
            return False # charge exceeds credit limit
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Customer payment to reduce balance"""
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Doe', 'Cali Savings',
                             '12345 6789 10', 2500) )
    wallet.append(CreditCard('John Doe', 'Cali Savings',
                             '12345 6789 11', 3500) )
    wallet.append(CreditCard('John Doe', 'Cali Savings',
                             '12345 6789 12', 5000) )
    print(f"Number of CCs is {len(wallet)}")

    for val in range(1, 17):
        for i in range(len(wallet)):
            wallet[i].charge(val*(i+1))

    for i in range(len(wallet)):
        print(f'Customer:\t{wallet[i].get_customer()}')
        print(f'Bank:\t\t{wallet[i].get_bank()}')
        print(f'Account:\t{wallet[i].get_account()}')
        print(f'Limit:\t\t{wallet[i].get_limit()}')
        print(f'Balance:\t{wallet[i].get_balance()}')
