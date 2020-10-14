class Library:
    __name = ''
    __books = []
    def __init__(self, name, books):
        self.__name = name
        self.set_books(books)

    def set_books(self, books):
        if not isinstance(books, list):
            self.__books = books
        else:
            self.__books = books
        return

    def find_books(self, author):
        for book in self.__books:
            if book.get_author() == author:
                print(book.get_name())
        return

    def append_book(self, book):
        self.__books.append(book)

    def get_information_about_book(self, book):
        return book.get_information()

    def get_information_about_books(self):
        for book in self.__books:
            print(book.get_information())

    def remove_books_of_this_author(self, author):
        self.__books_copied = []
        self.__books_copied = self.__books.copy()
        for book in self.__books_copied:
            if book.get_author() == author:
                self.__books.remove(book)
        return

class Book:
    __name = ''
    __author = ''
    __publisher = ''
    __date_of_issue = ''
    __ISBN_number = ''

    def __init__(self, name, author, publisher, date_of_issue, ISBN_number):
        self.__name = name
        self.__author = author
        self.__publisher = publisher
        self.__date_of_issue = date_of_issue
        self.__ISBN_number = ISBN_number

    def get_author(self):
        return self.__author
    def get_name(self):
        return self.__name
    def get_publisher(self):
        return self.__publisher
    def get_date_of_issue(self):
        return self.__date_of_issue
    def get_number(self):
        return self.__ISBN_number
    def get_information(self):
        return " ".join(["Название:", self.get_name(), "\n",
                         "Автор:", self.get_author(), "\n",
                         "Год издания:", self.get_date_of_issue(), "\n",
                         "Издательство: ", self.get_publisher(), "\n",
                         "ISBN номер: ", self.get_number(), "\n",])


def test_library():
    book_1 = Book('Практическая биология', 'Волошина', 'Издательство МЦНМО', '2017', '978-5-4439-1148-9')
    lib = Library('Имени Ленина', [book_1])
    book_2 = Book('Война и мир 1 том', 'Лев Толстой', 'Эксмо', '1990', '978-5-4439-1148-10')
    book_3 = Book('Война и мир 2 том', 'Лев Толстой', 'Питер', '1989', '978-6-4439-1148-9')
    book_4 = Book('Война и мир 3 том', 'Лев Толстой', 'Гамма', '1988', '978-5-4439-1147-9')
    lib.append_book(book_2)
    lib.append_book(book_3)
    lib.append_book(book_4)
    lib.get_information_about_books()
    lib.find_books('Лев Толстой')
    lib.remove_books_of_this_author('Лев Толстой')
    assert lib.find_books('Лев Толстой')

if __name__ == "__main__":
    test_library()

