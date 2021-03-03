import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Bramble", 6.0)
        self.drink2 = Drink("Long Vodka", 5.89)

        drinks = [self.drink1, self.drink2]
        self.pub = Pub("The Vaccine Arms", 1500.00, drinks)

    def test_pub_name(self):
        self.assertEqual("The Vaccine Arms", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1500, self.pub.till)
    
    def test_till_transaction(self):
        self.pub.till_transaction(100)
        self.assertEqual(1600, self.pub.till)

    def test_get_drink_name(self):
        find_drink = self.pub.find_drink_by_name("Long Vodka")
        self.assertEqual("Long Vodka", find_drink.name)
    
    def test_get_drink_price(self):
        find_drink_price = self.pub.find_drink_by_price(6.0)
        self.assertEqual("Bramble", find_drink_price.name)

    def test_sell_drink_to_customer(self):
        customer = Customer("Bob", 100.00)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1506.00, self.pub.till)
        self.assertEqual(94.00, customer.wallet)

    def test_sell_drink_to_customer_drink_not(self):
        customer = Customer("Bob", 100.00)
        self.pub.sell_drink(customer, "Beer")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(100.00, customer.wallet)

    def test_sell_drink_to_customer_drink_found_no_funds(self):
        customer = Customer("Bob", 3.00)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(3.00, customer.wallet)