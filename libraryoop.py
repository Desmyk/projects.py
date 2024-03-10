class Book:
    # initialize the Book object with a title, author and ISBN
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_checked_out = False
        
    def check_out(self):
        if self._is_checked_out:
            return True

    def return_book(self):
        if not self._is_checked_out:
            return self._is_checked_out
        
        
# represents a library with a list of books
class Library:
    # initializes a new library with empty list of books
    def __init__(self):
        self.books = []

    # adds a book to the library
    def add_book(self, book):
        self.books.append(book)

    # removes book from library by ISBN
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(isbn)
                return True
        print(f'Error:No book with ISBN {isbn} found')
        
    
     
    # checks out book by ISBN           
    def check_out(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.check_out()
                return True
        print(f"Error: No book found with ISBN {isbn}")
        
        
        
    def return_book(self, isbn):
        # Return a book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                return True
        print(f"Error: No book found with ISBN {isbn}")
        
        
        
    def list_books(self):
        # List all books in the library, including their checked out status
        for book in self.books:
            if book.check_out:
                status = "checked out"
            else:
                status = "not checked out"
        print(f"{book.title} by {book.author} (ISBN {book.isbn}) - {status}")
        

lib = Library()    
    
# Add books to library with different (titles, authors, ISBNs)
lib.add_book(Book('The end of an era', 'The Introvert', '4350' ))
lib.add_book(Book('A tale of two cities', 'Charles Dickens', '1239'))
lib.add_book(Book('The Alchemist', 'Paulo Coelho', '7865'))
lib.add_book(Book('True Times', 'The philosopher', '1985'))
lib.add_book(Book('The Hobbit', 'JRR Tolkien', '1234'))
lib.add_book(Book('The Wonders', 'Trey Green', '5678'))




# Check out book by ISBN
lib.check_out('1234')

# list all books in library
lib.list_books()

# Return book by ISBN
lib.return_book('4350')
        
lib.list_books()