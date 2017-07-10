def my_average(*args):
    length = len(args)
    return sum(args) / length


def main():
    user_input = input('Enter the required number of arguments: ')
    try:
        values = user_input.split(sep=' ')
        values = list(map(int, values))
        result = my_average(*values)
        print('The arithmetic mean value:', result)
    except ValueError as error:
        print('Error: ', error)

if __name__ == '__main__':
    main()
