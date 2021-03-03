import unittest

from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Vaccine Arms", 1500.00, [])