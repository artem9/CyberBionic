class Book:
    def __init__(self, *args):
        '''
        :param args:
         1 - Title
         2 - Author
         3 - Publish Date
         4 - Genre
        '''

        try:
            self.title = args[0]
        except IndexError:
            self.title = ''
        try:
            self.author = args[1]
        except IndexError:
            self.author = ''
        try:
            self.pub_date = args[2]
        except IndexError:
            self.pub_date = ''
        try:
            self.genre = args[3]
        except IndexError:
            self.genre = ''

        self.feedbacks = []

    def __str__(self):

        book_info = '\n* Title: {}\n* Author: {}\n* Publish Date: {}\n* Genre: {}\n* Comments:\n'.format(self.title,
                                                                                                      self.author,
                                                                                                      self.pub_date,
                                                                                                      self.genre)

        comments = ''
        size_of_comments = len(self.feedbacks)
        if size_of_comments > 0:
            comments = '\n'.join(map(str, self.feedbacks))
        else:
            comments = 'No comments yet.'

        return book_info + comments

    def __repr__(self):
        return '\n%s Title: %s, Author: %s, Publish Date: %s, Genre: %s %s\n' % ('*' * 6, self.title, self.author,
                                                                               self.pub_date, self.genre, '*' * 6)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and \
               self.pub_date == other.pub_date and self.genre == other.genre

    def __ne__(self, other):
        return not (self == other)

    def get_info_about_book(self):
        print('\nTitle: %s\nAuthor: %s\nPublish Date: %s\nGenre: %s\n' %
              (self.title, self.author, self.pub_date, self.genre))


class BookFeedback:
    def __init__(self, comment):
        self.feedback = comment

    def __str__(self):
        return '\t- %s' % self.feedback


def main():
    # examples of the books
    book1 = Book('Steve Jobs', 'Simon & Schuster', '2015-09-15', 'Autobiography')
    book2 = Book('Fifty Shades Darker', 'E. L. James', '2012-04-17', 'Novel')
    book3 = Book('Harry Potter and the Deathly Hallows (Book 7)', 'J. K. Rowling ', '2009-07-07', 'Fantasy')

    # copy of yhe second book
    book4 = Book('Fifty Shades Darker', 'E. L. James', '2012-04-17', 'Novel')

    # checking between instances of the Book
    print('Book1 == Book2:', book1 == book2)
    print('Book2 == Book4:', book2 == book4)

    print('Book4 != Book1:', book4 != book1)
    print('Book4 != Book2:', book4 != book2)

    # feedback functionality
    # lets add few comments for each book
    book1.feedbacks.append(BookFeedback('Nice story!'))
    book1.feedbacks.append(BookFeedback('This person is now my idol.'))
    book2.feedbacks.append(BookFeedback('Book more interesting instead of movie.'))

    # different output of the object Book
    print(book1)
    book2.get_info_about_book()
    print(repr(book3))

if __name__ == '__main__':
    main()
