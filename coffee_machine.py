class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, revenue,
                 state='Choosing action'):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.revenue = revenue
        self.state = state

    def __repr__(self):
        return 'CoffeeMachine(water={}, milk={}, beans={}, cups={}, \
                revenue={}, state={}'.format(self.water, self.milk,
                                             self.beans, self.cups,
                                             self.revenue, self.state)

    def buy(self, action):
        """Buy espresso, latte or cappuccino if enough inventory on hand."""
        espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
        latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
        cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}
        if action == '1':
            self.check_levels(espresso)
        elif action == '2':
            self.check_levels(latte)
        elif action == '3':
            self.check_levels(cappuccino)
        elif action == 'back':
            self.state = 'Choosing action'

    def check_levels(self, recipe):
        """Determines if enough inventory to produce drink. Prints missing
        ingredient if not and resets state.
        """
        if self.water >= recipe['water'] and self.milk >= recipe['milk'] \
                and self.beans >= recipe['beans']:
            print('I have enough resources, making you a coffee!\n')
            self.dispense_drink(recipe)
            self.state = 'Choosing action'
        else:
            if recipe['water'] > self.water:
                print('Sorry, not enough water!\n')
            elif recipe['milk'] > self.milk:
                print('Sorry, not enough milk!\n')
            elif recipe['beans'] > self.beans:
                print('Sorry, not enough beans!\n')
            self.state = 'Choosing action'

    def fill(self, water, milk, beans, cups):
        """Refill inventory."""
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups
        self.state = 'Choosing action'

    def take(self):
        """Collect revenue."""
        print(f'I gave you ${self.revenue}\n')
        self.revenue = 0
        self.state = 'Choosing action'

    def stock_status(self):
        """Prints current inventory levels."""
        print(f'This coffee machine has: \
            \n{self.water} of water \
            \n{self.milk} of milk \
            \n{self.beans} of beans \
            \n{self.cups} of disposable cups \
            \n{self.revenue} of money\n')
        self.state = 'Choosing action'

    def dispense_drink(self, recipe):
        """Subtract ingredients for drink and add revenue."""
        self.water -= recipe['water']
        self.milk -= recipe['milk']
        self.beans -= recipe['beans']
        self.cups -= 1
        self.revenue += recipe['cost']


def main():
    coffee = CoffeeMachine(400, 540, 120, 9, 550)
    while coffee.state != 'Shutting down':
        if coffee.state == 'Choosing action':
            action = str(input('Write action (buy, fill, take, remaining,'
                               + ' exit):\n')).strip().lower()
            if action == 'buy':
                coffee.state = 'Buying coffee'
            elif action == 'fill':
                coffee.state = 'Refilling inventory'
            elif action == 'take':
                coffee.state = 'Cashing out'
            elif action == 'remaining':
                coffee.state = 'Checking inventory'
            elif action == 'exit':
                coffee.state = 'Shutting down'
        elif coffee.state == 'Buying coffee':
            action = str(input('What do you want to buy? 1 - espresso'
                               + ' 2 - latte, 3 - cappuccino:\n')).strip()
            coffee.buy(action)
        elif coffee.state == 'Refilling inventory':
            add_water = int(input('Write how many ml of water do you want'
                                  + ' to add:\n'))
            add_milk = int(input('Write how many ml of water do you want to'
                                 + ' add:\n'))
            add_beans = int(input('Write how many grams of coffee beans do'
                                  + ' you want to add:\n'))
            add_cups = int(input('Write how many disposable cups of coffee'
                                 + ' do you want to add:\n'))
            coffee.fill(add_water, add_milk, add_beans, add_cups)
        elif coffee.state == 'Cashing out':
            coffee.take()
        elif coffee.state == 'Checking inventory':
            coffee.stock_status()


if __name__ == '__main__':
    main()
