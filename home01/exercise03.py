class Temperature:
    '''
        To convert temperatures in degrees Celsius to
        Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
    '''
    def __init__(self, value=0):
        self.temperature = value

    @property
    def get_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def get_celsius(self):
        return self._temperature

    def set_temperature(self, value):
        '''
            Temperatures cannot go below -273 degree Celsius, also called the absolute zero
        '''
        if value < -273:
            raise ValueError('Temperatures cannot go below -273 degree Celsius')
        self._temperature = value

    temperature = property(get_celsius, set_temperature)


def main():
    input_value = int(input('Please input temperature (in Celsius degrees): '))
    temp = Temperature()
    temp.temperature = input_value
    print('\n- Temperature in Celsius degrees: {}\n- Temperature in Fahrenheit '
          'degrees: {}\n'.format(str(temp.temperature), str(temp.get_fahrenheit)))


if __name__ == '__main__':
    main()
