import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Bramble", 6.0)
        self.drink2 = Drink("Long Vodka", 5.89)

        self.drinks = [self.drink1, self.drink2]
        self.pub = Pub("The Vaccine Arms", 1500.00, self.drinks)

    def test_pub_name(self):
        self.assertEqual("The Vaccine Arms", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1500, self.pub.till)