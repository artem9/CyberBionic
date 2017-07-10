import string


def ordering_words(value):
    list_of_words = [word.strip(string.punctuation) for word in value.split()]
    list_of_words.sort(key=lambda x: x.lower())
    print(list_of_words)


def main():
    user_input = input('Please enter text: ')
    ordering_words(user_input)


if __name__ == '__main__':
    main()
