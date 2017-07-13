class MyLinks:
    def __init__(self):
        self.links = {}

    def add_link(self):
        user_input = input('Please enter URL: ')
        short_name = None
        while not short_name or short_name in self.links:
            short_name = input('Please enter short name: ')
            if short_name in self.links:
                print('This name already present in list: '
                      'url: %s' % self.links[short_name])
        self.links[short_name] = user_input

    def get_link(self):
        user_input = input('Please enter url name: ')
        result = self.links.get(user_input, None)
        return result


def main():
    links = MyLinks()

    while True:
        print('1. Add\n'
              '2. Find\n'
              '3. Exit')
        choice = input('Please input operation: ')
        if choice == '1':
            links.add_link()
        if choice == '2':
            search = links.get_link()
            if search:
                print('Url address:', search)
            else:
                print('Current link does not exist.')
        if choice == '3':
            break


if __name__ == '__main__':
    main()