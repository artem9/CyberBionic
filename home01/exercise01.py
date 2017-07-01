class Automobile:
    def __init__(self):
        self.manufacturer = ''
        self.model = ''
        self.color = ''
        self.engine_capacity = ''
        self.type_of_fuel = ''
        self.production_year = ''

    def set_parameters(self, manufacturer, model, color, capacity, fuel, production):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine_capacity = capacity
        self.type_of_fuel = fuel
        self.production_year = production

    def read_parameters(self):
        print('*' * 40)
        print('Manufacturer: {}\nModel: {}\nColor: {}\nEngine_capacity: {}\n'
              'Type of fuel: {}\nProduction Year: {}'.format(self.manufacturer,
                                                             self.model, self.color,
                                                             self.engine_capacity, self.type_of_fuel,
                                                             self.production_year))
        print('*' * 40)


class SellerAuto:
    def __init__(self):
        self.list_available_automobiles = []

    def car_purchase(self, car):
        self.list_available_automobiles.append(car)

    def car_sell(self, car):
        self.list_available_automobiles.remove(car)

    def show_available_cars(self):
        if not self.list_available_automobiles:
            print('There are no cars yet.')
        else:
            return self.list_available_automobiles

    def search_car(self):
        if not self.list_available_automobiles:
            print('Seller do not have any cars in in stock.')
            return

        while True:
            producer = str(input('Please enter Manufacturer: '))
            model = str(input('Please enter Model: '))

            for item in self.list_available_automobiles:
                if item.manufacturer == producer and item.model == model:
                    print('Car has been found!')
                    return item
                else:
                    choice = str(input('Car not found, do you want to continue? (y/n): '))
                    if choice == 'n':
                        return


def main():
    # test class Automobile
    test_auto = Automobile()
    test_auto2 = Automobile()

    # fill in parameters
    test_auto.set_parameters('Ford', 'Focus GT', 'Blue', 2.0, 'Petrol', '2015-02-04')
    test_auto2.set_parameters('Mazda', 'CX3', 'Silver', 2.4, 'Diesel', '2012-01-09')

    # test class Seller
    winner_auto = SellerAuto()

    # seller buy new car
    winner_auto.car_purchase(test_auto)
    winner_auto.car_purchase(test_auto2)

    # show information about automobile
    print('*' * 40)
    print('List of available cars: ')
    available_cars = winner_auto.show_available_cars()
    for item in available_cars:
        Automobile.read_parameters(item)

    # find you car
    my_car = winner_auto.search_car()

    if my_car:
        choice = str(input('Do you want to buy it? (y/n) '))
        if choice == 'y':
            winner_auto.car_sell(my_car)
            print('Congratulations, you bought a new car!\n')

            print('Updated list of available cars: ')
            for item in available_cars:
                Automobile.read_parameters(item)

if __name__ == '__main__':
    main()
