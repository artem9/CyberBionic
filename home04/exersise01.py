class ReverseSequence:
    def __init__(self, sequence):
        self.index = len(sequence) - 1
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        next_value = self.sequence[self.index]
        self.index -= 1

        return next_value

if __name__ == '__main__':
    new_list = [*range(15)]
    print('Original order :', *new_list)
    my_reverse = ReverseSequence(new_list)
    print('My reverse: ', *my_reverse)
