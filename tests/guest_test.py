import unittest

from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink


class TestGuest (unittest.TestCase):
    def setUp(self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest = Guest('David',25,50,self.song_01)

    def test_guest_name(self):
        self.assertEqual('David', self.guest.name)

    def test_guest_age(self):
        self.assertEqual(25, self.guest.age)

    def test_guest_wallet(self):
        self.assertEqual(50,self.guest.wallet)

    def test_guest_favourite_song(self):
        self.assertEqual('Billie Jean', self.guest.favourite_song.name)

    def test_remove_cash_from_wallet(self):
        self.guest.remove_cash(10)
        self.assertEqual(40, self.guest.wallet)

    def test_add_cash_cash_to_tab(self):
        self.guest.add_to_tab(30)
        self.assertEqual(30, self.guest.tab)

    def test_remove_cash_from_tab(self):
        self.guest.add_to_tab(30)
        self.guest.remove_from_tab(20)
        self.assertEqual(10,self.guest.tab)

    def test_add_drink_to_guest(self):
        self.drink_01 = Drink('beer', 10)
        self.guest.add_drink_to_guest(self.drink_01)
        self.assertEqual(self.drink_01, self.guest.guest_drink[0])