import unittest

from classes.bar import Bar
from classes.drink import Drink
from classes.guest import Guest
from classes.song import Song

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


    def test_check_guest_has_enough_cash__True (self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest =Guest('David',25,50,self.song_01)
        self.bar.add_drink(self.drink_01)
        drink = self.bar.find_drink('beer')
        self.bar.check_wallet(self.guest,drink)
        self.assertEqual(True,self.bar.check_wallet(self.guest,drink))


    def test_check_guest_has_enough_cash__False (self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest =Guest('David',25,5,self.song_01)
        self.bar.add_drink(self.drink_01)
        self.bar.check_wallet(self.guest,self.drink_01)
        self.assertEqual(False,self.bar.check_wallet(self.guest, self.drink_01))
        

    # adding cash to guest tab and will pay tab via a method in karaoke_bar class

    def test_sell_drink_to_guest(self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest =Guest('David',25,50,self.song_01)
        self.bar.add_drink(self.drink_01)
        self.bar.add_drink(self.drink_02)
        self.bar.sell_drink(self.guest,'beer')
        self.assertEqual(40,self.guest.wallet)
        self.assertEqual(10 ,self.guest.tab)
        self.assertEqual(self.drink_02,self.bar.drinks[0])
        self.assertEqual(self.drink_01, self.guest.guest_drink[0])








    

    

    