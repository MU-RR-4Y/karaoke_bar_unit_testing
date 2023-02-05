class Room:
    def __init__(self, number, capacity, time_slot, fee ):
        self.number = number
        self.capacity = capacity
        self.time_slot = time_slot
        self.fee = fee
        self.guest_list = []
        self.playlist = []
        self.current_song = ''
        self.current_song_time = 0
        self.time_taken = 0

    def check_capacity(self, room):
        if len(room.guest_list) < room.capacity:
            return True
        else:
            return False

    def add_guest(self,guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def empty_room(self):
        self.guest_list.clear()

    def add_song(self,song):
        self.playlist.append(song)

    def time_left(self, song_added):
        current_time_taken = 0
        for song in self.playlist:
            current_time_taken += song_added.time_of_song

        if song_added.time_of_song <= (self.time_slot - current_time_taken):
            return True
        else:
            return False

    def charge_fee(self, guest):
        guest.tab += self.fee

    def remove_song_from_playlist(self,playlist):
        self.playlist.pop(0)
               
    
    def play_song(self, playlist):
        self.current_song = self.playlist[0]
        self.current_song_time = self.playlist[0].time_of_song
        self.time_taken += self.playlist[0].time_of_song



# still working on this - not sure best way to test tracking time taken

    def next_song_playing(self,current_song):
        while self.current_song_time > 0:
            self.current_song_time -= 1
        
        if self.current_song_time == 0:
            self.remove_song_from_playlist(self.playlist)
            self.play_song(self.playlist)


        



