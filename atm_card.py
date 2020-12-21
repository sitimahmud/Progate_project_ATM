class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def info(self):
        return self.defaultPin + ': $' + str(self.defaultBalance)

    def get_default_pin(self):
        return self.defaultPin

    def get_default_balance(self):
        return self.defaultBalance