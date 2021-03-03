import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alex Kinsey", 100.00, 26, 3)

    def test_customer_has_name(self):
        self.assertEqual("Alex Kinsey", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(100.0, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(90.00, self.customer.wallet)

    def test_customer_drunkeness(self):
        self.assertEqual(3, self.customer.drunkeness)
    
    def test_customer_increase_drunkness(self):
        self.customer.customer_drunkeness(10)
        self.assertEqual(13, self.customer.drunkeness)