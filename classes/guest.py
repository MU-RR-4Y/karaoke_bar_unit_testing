class Guest:
    def __init__(self,name,age,wallet,favourite_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.guest_drink = []
        self.tab = 0

    def remove_cash(self, amount):
        self.wallet -= amount

    def add_to_tab(self, amount):
        self.tab += amount

    def remove_from_tab(self, amount):
        self.tab -= amount

    def add_drink_to_guest(self,drink):
        self.guest_drink.append(drink)

