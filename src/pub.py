class Pub:
    def __init__(self,name,till,drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def till_transaction(self, amount):
        self.till += amount

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
        return None

    def find_drink_by_price(self, price):
        for drink in self.drinks:
            if drink.price == price:
                return drink
        return None
    
    def sell_drink(self, customer, drink_name):
        if customer.age < 18:
            return
        
        if customer.drunkeness > 10:
            return

        drink = self.find_drink_by_name(drink_name)
        if not drink:
            return

        if customer.wallet < drink.price:
            return
        
        customer.reduce_wallet(drink.price)
        self.till_transaction(drink.price)