import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53 )

    def test_check_name_of_song(self):
        self.assertEqual('Billie Jean', self.song_01.name)

    def test_check_artist(self):
        self.assertEqual('Michael Jackson', self.song_01.artist)

    def test_check_time_of_song(self):
        self.assertEqual(4.53, self.song_01.time_of_song)
