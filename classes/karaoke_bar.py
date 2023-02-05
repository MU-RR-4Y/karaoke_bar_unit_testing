class Karaoke_bar:
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def pay_tab(self, guest):
        guest.remove_cash(guest.tab)
        self.till += guest.tab


    
        
