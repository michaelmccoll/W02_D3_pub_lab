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