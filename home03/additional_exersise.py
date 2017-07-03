class Error(Exception):
    '''Base class for other exceptions'''
    pass


class TooLowTemperature(Error):
    '''Temperatures cannot go below -273 degree Celsius, also called the absolute zero
    This is child of Class Error'''
    pass


def main():
    lower_bound = -273.0
    temperature = float(input('Please input temperature (in Celsius degrees): '))
    try:
        if temperature < lower_bound:
            raise TooLowTemperature
        else:
            print('Temperature in Fahrenheit: %s' % str(temperature * 1.8 + 32.0))
    except TooLowTemperature:
        print('Temperatures cannot go below -273 degree Celsius.')

    print('End of program!')

if __name__ == '__main__':
    main()