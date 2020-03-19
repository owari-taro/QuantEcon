class Consumer:

    def __init__(self, wealth):
        def wealth = wealth

    def earn(self, y):
        self.wealth += y

    def spend(self, x):
        new_wealth = self.wealth-x
        if new_wealth < 0:
            raise Exception("insufficient funds")
        self.wealth = new_wealth
