def comparing_strings(value1, value2):
    set1 = set(value1)
    set2 = set(value2)
    return set1.intersection(set2)


def main():
    first_input = input('Please enter first value(string): ')
    second_input = input('Please enter second value(string): ')

    result = comparing_strings(first_input, second_input)
    print('Common symbols:')
    for symbol in result:
        print(symbol, end=' ')


if __name__ == '__main__':
    main()