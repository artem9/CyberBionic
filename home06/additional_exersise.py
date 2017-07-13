def operation_with_dict(**kwargs):
    for name, age in kwargs.items():
        print(name, 'is', age)


def main():
    my_dict = {'John': 21, 'Mary': 32, 'Mike': 26}
    operation_with_dict(**my_dict)


if __name__ == '__main__':
    main()