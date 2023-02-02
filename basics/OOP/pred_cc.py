#!/usr/bin/env python3

from cc import CreditCard

# below syntax shows we inherits the CreditCard class
# NOTE: that in both charge() and process_month() methods, the protected member
#       _balance is directly accessed. There is no formal access control in Python,
#       and this method is OK, however the parent CreditCard class could also have
#       intended to make this member private (cannonically with a double-underscore
#       as __balance) and used setter/getter methods (e.g. get_balance()/_set_balance())
#       to break the direct dependency on the inherited member (say if the internal design
#       of the class changes). In Python, protected members usually are prepended with a
#       single underscore (intent to be hidden from public use, but can be used by subclasses)
#       and private members a double underscore (only accessible in defining class)
class PredatoryCreditCard(CreditCard):
    """Extends basic Credit Card class that compounds interest and fees"""

    def __init__(self, customer, bank, accnt, limit, apr):
        """Creates a new predatory credit card instance.

        Initial balance is 0.

        customer: name of the customer (e.x. 'John Doe')
        bank:     name of the bank (e.x. 'Chase')
        accnt:    account identifier (e.g. '1234 5678 90')
        limit:    credit limit (in USD)
        apr:      annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """
        super().__init__(
            customer, bank, accnt, limit
        )  # calls constructor in parent class
        self._apr = apr

    def charge(self, price):
        """Charge to account balance 'price' amount, assuming sufficient credit
        limit.

        Returns True if charge was processed, False if charge was declined due
        to insufficient credit.

        Extends charge() functionality in parent CreditCard class by also adding a $5
        fee if charge is denied.
        """
        was_success = super().charge(price)  # call inherited method
        if not was_success:
            self._balance += 5
        return was_success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
