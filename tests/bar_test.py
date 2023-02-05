import unittest

from classes.bar import Bar
from classes.drink import Drink

class TestBar(unittest.TestCase):

    # drink_01 = ('beer', 10)
    # drink_02 = ('wine', 20)
    # drink_03 = ('spirits', 15)
    # drinks = [drink_01, drink_02, drink_03]
    
    def setUp(self):
        self.drink_01 = Drink('beer', 10)
        self.drink_02 = Drink('wine', 20)
        self.drink_03 = Drink('spirits', 15)
        self.bar = Bar('Karaoke Bar')

    def test_bar_name(self):
        self.assertEqual('Karaoke Bar', self.bar.name)    

    def test_bar_has_drink(self):
        self.assertEqual(0, len(self.bar.drinks))

    def test_can_add_drink_to_bar(self):
        self.bar.add_drink(self.drink_01)
        self.bar.add_drink(self.drink_02)
        self.assertEqual('wine' , self.bar.drinks[1].name)

    def test_can_remove_drink_from_bar(self):
        self.bar.add_drink(self.drink_01)
        self.bar.add_drink(self.drink_02)
        self.bar.add_drink(self.drink_03)
        self.bar.remove_drink(self.drink_02)
        self.assertEqual([self.drink_01, self.drink_03], self.bar.drinks)

    def test_find_drink_by_name__have_drink(self):
        self.bar.add_drink(self.drink_01)
        result = self.bar.find_drink('beer')
        self.assertEqual(self.drink_01, result)

    def test_find_drink_by_name__do_not_have_drink(self):
        self.bar.add_drink(self.drink_01)
        result = self.bar.find_drink('wine')
        self.assertEqual('drink not found', result)






    # def test_sell_drink_to_guest(self):
    #     self.bar.add_drink(self.drink_01)
    #     self.bar.add_drink(self.drink_02)
    #     self.bar.add_drink(self.drink_03)
    #     self.sell_drink('beer')
    #     self.assertEqual







    

    

    