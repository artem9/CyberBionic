def my_reverse(sequence):
    index = len(sequence) - 1
    while index >= 0:
        yield sequence[index]
        index -= 1

if __name__ == '__main__':
    new_list = [*range(12)]
    print('Original order: ', *new_list)
    ordered_list = my_reverse(new_list)
    print('My reverse: ', *ordered_list)

