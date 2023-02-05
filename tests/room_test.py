import unittest

from classes.room import Room
# from classes.karaoke_bar import Karaoke_bar
from classes.song import Song
from classes.guest import Guest


class TestRoom (unittest.TestCase):
    def setUp(self):
        self.song_01 = Song('Billie Jean', 'Michael Jackson', 4.53)
        self.guest = Guest('David',25,50,self.song_01)

        self.room = Room(1,4,10,15)
          

# check room number
    def test_check_room_number(self):
        self.assertEqual(1, self.room.number)
# check capacity
    def test_check_room_capcity(self):
        self.assertEqual(4,self.room.capacity)


# check number of guest in room
    def test_number_of_guests_in_room(self):
        self.assertEqual(0, len(self.room.guest_list))

# check number of songs on playlist
    def test_check_number_of_songs_on_playlist(self):
        self.assertEqual(0, len(self.room.playlist))


# check timeslot - the time guests have the room for
    def test_check_time_slot(self):
        self.assertEqual(10, self.room.time_slot)
# check fee for room
    def test_check_room_fee(self):
        self.assertEqual(15, self.room.fee)


# check in guests
    def test_add_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(self.guest, self.room.guest_list[0])

# check if room has capacity
    def test_capacity__room_is_not_full(self):
        space_in_room = self.room.check_capacity(self.room)
        self.assertEqual(True, space_in_room)


    def test_capacity__room_is_full(self):
        self.room = Room(1,3,10,15)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        space_in_room = self.room.check_capacity(self.room)
        self.assertEqual(False, space_in_room)

       
# check out guests

        # individually remove

    def test_remove_guest(self):
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.guest_02 = Guest('John',30,75,self.song_02)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_02)
        self.room.remove_guest(self.guest)
        self.assertEqual(self.guest_02, self.room.guest_list[0])

        # empty room at end 

    def test_empty_room (self):
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.guest_02 = Guest('John',30,75,self.song_02)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_02)
        self.room.empty_room()
        self.assertEqual(0, len(self.room.guest_list))

        
# add songs to playlist
        
    def test_add_song_to_playlist(self):
        self.room.add_song(self.song_01)
        self.assertEqual(self.song_01, self.room.playlist[0])

   # checking total time of songs on playlist against time_slot to se if there is time to request song
   
    def test_time_left_to_request_song__time_available(self):
        self.room = Room(1,4,10,15)
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.room.add_song(self.song_01)
        result = self.room.time_left(self.song_01)
        self.assertEqual(True, result)

    def test_time_left_to_request_song__time_not_available(self):
        self.room = Room(1,4,10,15)
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.room.add_song(self.song_01)
        self.room.add_song(self.song_02)
        result = self.room.time_left(self.song_01)
        self.assertEqual(False, result)
    
# charge fee for using a room - added to guest tab

    def test_charge_fee_for_room(self):
        self.room.charge_fee(self.guest)
        self.assertEqual(15, self.guest.tab)

# guest hears favourite song

    def test_test_play_song(self):
        self.room.add_song(self.song_01)
        self.room.play_song(self.room.playlist)
        self.assertEqual(self.song_01, self.room.current_song)
        self.assertEqual(4.53, self.room.current_song_time)

    def test_remove_song(self):
        self.song_02 = Song('I want you back', 'Jackson 5', 2.56)
        self.room.add_song(self.song_01)
        self.room.add_song(self.song_02)
        self.room.remove_song_from_playlist(self.room.playlist)
        self.assertEqual(self.song_02, self.room.playlist[0])


    # def test_song_playing(self):
    #     self.room.add_song(self.song_01)
    #     self.room.play_song(self.room.playlist)
    #     self.room.song_playing(self.room.current_song)


    #     self.assertEqual(True, is_song_playing)

    # def test_song_playing__False(self):
    #     self.room.add_song(self.song_01)
    #     self.room.play_song(self.room.playlist)
    #     self.room.song_playing(self.room.current_song)


    #     self.assertEqual(False, is_song_playing)