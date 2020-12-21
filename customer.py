from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin=1234, custBalance=1000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def withdrawBalance(self, nominal):
        self.custBalance = self.custBalance - nominal
        return self.custBalance

    def depositBalance(self, nominal):
        self.custBalance = self.custBalance + nominal
        return self.custBalance

    def checkBalance(self):
        return self.custBalance

    def pin_atm(self):
        return self.custPin

    def new_pin(self, newpin):
        self.custPin = newpin
        return self.custPin
 
