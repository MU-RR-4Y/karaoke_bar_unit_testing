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

        