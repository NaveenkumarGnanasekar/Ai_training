class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{title}'")
                return
        print(f"'{title}' is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned '{title}'")
                return
        print(f"'{title}' was not borrowed")
library = Library()

book1 = Book("Python Basics", "John Doe")
book2 = Book("Data Structures", "Jane Smith")

library.add_book(book1)
library.add_book(book2)

library.borrow_book("Python Basics")
library.borrow_book("Python Basics") 
library.return_book("Python Basics")
