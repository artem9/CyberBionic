class GraphicObject:
    def __init__(self, side):
        self.side = side

    def click(self):
        try:
            self.click_me()
        except AttributeError:
            print(type(self).__name__, 'is not clickable')


class Rectangle(GraphicObject):
    def __init__(self, left_side, top_side, label=''):
        super().__init__(side=left_side)
        self.left_side = self.side
        self.top_side = top_side
        self.label = label

    def draw(self):
        if self.label:
            padded_label = ' [' + self.label + '] '
        else:
            padded_label = self.label
        length_of_label = len(padded_label)

        left_padding = round((self.top_side - length_of_label) / 2)
        left = '+' * left_padding
        right = '+' * (self.top_side - left_padding - length_of_label)

        for i in range(self.left_side):
            if i == round(self.left_side / 2):
                print(left, padded_label, right, sep='')
            else:
                print('+' * self.top_side)


class ClickableObject:
    def click_me(self):
        print(type(self).__name__, 'clicked')


class Button(Rectangle, ClickableObject):
    def __init__(self, height, width, text=''):
        if not text:
            text = type(self).__name__
        super().__init__(height, width, text)


def main():

    my_rectangle = Rectangle(5, 17)
    my_rectangle.draw()
    my_rectangle.click()

    button = Button(5, 18)
    button.draw()
    button.click()


if __name__ == '__main__':
    main()
