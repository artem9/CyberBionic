def sorting_numbers(input_value):
    list_of_value = input_value.split(sep=' ')
    list_of_value = list(map(int, list_of_value))
    list_of_value.sort()
    return list_of_value


def main():
    values = input('Please enter numbers: ')
    new_list = sorting_numbers(values)
    print(*new_list)


if __name__ == '__main__':
    main()
