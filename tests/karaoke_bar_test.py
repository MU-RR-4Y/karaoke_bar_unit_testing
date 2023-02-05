import unittest

from classes.karaoke_bar import Karaoke_bar
from classes.bar import Bar
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink
# song import requied to add a catelogue of songs to pick from

class TestKaraoke_bar(unittest.TestCase):
    def setUp(self):
        self.room_01 = Room(1,4,10,15)        
        self.room_02 = Room(2,6,20,30) 
        rooms = [self.room_01, self.room_02]

        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest_01 = Guest('David',25,50,self.song_01)
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.guest_02 = Guest('John',30,75,self.song_02)

        guests = [self.guest_01, self.guest_02]

        self.karaoke_bar = Karaoke_bar('Motown Karaoke', 1000)

    def test_karaoke_name (self):
        self.assertEqual('Motown Karaoke', self.karaoke_bar.name)

    def test_karaoke_till (self):
        self.assertEqual(1000, self.karaoke_bar.till)

    def test_settle_bill(self):
        self.drink_01 = Drink('beer', 10)
        self.bar = Bar('Karaoke Bar')
        # add charge for buying a drink
        self.bar.add_drink(self.drink_01)
        self.bar.sell_drink(self.guest_01,'beer')
        # add fee for using room
        self.room_01.add_guest(self.guest_01)
        self.room_01.charge_fee(self.guest_01)
        
        self.karaoke_bar.pay_tab(self.guest_01)
        self.assertEqual(25, self.guest_01.wallet)
        self.assertEqual(1025,self.karaoke_bar.till)
