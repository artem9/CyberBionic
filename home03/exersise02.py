class MyCalculator:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        self.dict_of_functions = {1: self.sum, 2: self.dist, 3: self.mult,
                                  4: self.div, 5: self.exp}

    def sum(self):
        return self.first_num + self.second_num

    def dist(self):
        return self.first_num - self.second_num

    def mult(self):
        return self.first_num * self.second_num

    def div(self):
        return self.first_num / self.second_num

    def exp(self):
        return self.first_num ** self.second_num

    def run_function(self, number):
        return self.dict_of_functions.get(number)()


class UnknownOperation(Exception):
    def __str__(self):
        return 'Unsupported operation'


class NoValidNumbers(Exception):
    def __str__(self):
        return 'In calculations only numbers can be used!'


def main():
    print()
    list_operations = {1: 'Sum of elements', 2: 'Subtraction of elements', 3: 'Multiplication of elements',
                       4: 'Division of elements', 5: 'Exponentiation of elements'}

    for item in list_operations:
        print('-{}- {};'.format(item, list_operations[item]))

    try:
        while True:
            try:
                operation = int(input('\nPlease select # operation: '))
                if operation not in list_operations.keys():
                    raise UnknownOperation
                break
            except (ValueError, UnknownOperation):
                print('You enter invalid character. Please use numbers from list above')
                continue

        try:
            value_1 = float(input('Enter #1: '))
            value_2 = float(input('Enter #2: '))
        except ValueError:
            raise NoValidNumbers

        result = MyCalculator(value_1, value_2)
        print('Result: {}'.format(result.run_function(operation)))

    except UnknownOperation:
        print('Program do not support entered operation!')
    except NoValidNumbers:
        print('Please use only numbers in your calculations!')
    except ZeroDivisionError as error:
        print('{}'.format(error))


if __name__ == '__main__':
    main()
