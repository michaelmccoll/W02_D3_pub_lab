class Customer:
    def __init__(self,name,wallet,age, drunkeness = None):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness or 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def customer_drunkeness(self,amount):
        self.drunkeness += amount
