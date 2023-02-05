class Bar:
    def __init__(self,name):
        self.name = name
        self.drinks = []

    def add_drink(self, drink_added):
        self.drinks.append(drink_added)

    def remove_drink(self, drink_removed):
        self.drinks.remove(drink_removed)

    def find_drink(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
            else: 
                return 'drink not found'

    def check_wallet(self, guest, drink):
        if guest.wallet >= drink.price:
            return True
        else:
            return False

    def sell_drink(self, guest, drink):
        
        drink_purchased = self.find_drink(drink)
        if self.check_wallet(guest, drink_purchased) == True:
            guest.remove_cash(drink_purchased.price)
            guest.add_to_tab(drink_purchased.price)
            self.remove_drink(drink_purchased)
            guest.add_drink_to_guest(drink_purchased)
            
           


        