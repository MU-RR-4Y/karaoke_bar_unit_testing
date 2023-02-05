import unittest

from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_01 = Drink('beer', 10)

    def test_check_drink_name(self):
        self.assertEqual('beer', self.drink_01.name)

    def test_check_drink_price(self):
        self.assertEqual(10 , self.drink_01.price)

        