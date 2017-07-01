class Transport:
    def __init__(self, movement_space='', max_speed=0, number_of_passengers=0):
        self.movement_space = movement_space
        self.max_speed = max_speed
        self.number_of_passengers = number_of_passengers

    def __str__(self):
        basic_info = '\nObject "{}", with following parameters: \n- Movement Space: {}' \
                     '\n- Max Speed: {}\n- Number of Passengers: {}'.format(type(self).__name__, self.movement_space,
                                                                            self.max_speed, self.number_of_passengers)
        return basic_info


class GroundTransport(Transport):
    def __init__(self, max_speed=0, number_of_passengers=0, type_of_fuel=''):
        super().__init__(movement_space='Ground', max_speed=max_speed, number_of_passengers=number_of_passengers)
        self.type_of_fuel = type_of_fuel

    def __str__(self):
        return super().__str__() + '\n- Type of Fuel: {}'.format(self.type_of_fuel)


class AirTransport(Transport):
    def __init__(self, max_speed=0, number_of_passengers=0, max_flight_altitude=0):
        super().__init__(movement_space='Air', max_speed=max_speed, number_of_passengers=number_of_passengers)
        self.max_flight_altitude = max_flight_altitude

    def __str__(self):
        return super().__str__() + '\n- Maximum flight altitude: {}'.format(self.max_flight_altitude)


class WaterTransport(Transport):
    def __init__(self, max_speed=0, number_of_passengers=0, cargo_transportation=False):
        super().__init__(movement_space='Water', max_speed=max_speed, number_of_passengers=number_of_passengers)
        self.cargo_transportation = cargo_transportation

    def __str__(self):
        return super().__str__() + '\n- Cargo transportation: {}'.format(self.cargo_transportation)


trans = Transport('Space', 300, 250)
ground_trans = GroundTransport(220, 30, 'Petrol')
air_trans = AirTransport(400, 70, 3000)
water_trans = WaterTransport(80, 1500, True)

print(trans)
print(ground_trans)
print(air_trans)
print(water_trans)
