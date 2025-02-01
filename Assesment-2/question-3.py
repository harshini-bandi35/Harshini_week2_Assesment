'''You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to 
    display book details.'''

class Book:
    def __init__(self,isbn,title,author):
        self.isbn=isbn
        self.title=title
        self.author=author
    def display_book_details(self):
        print(f"isbn : {self.isbn}, title : {self.title}, author : {self.author}")
book1=Book(101,"It ends with us","coolen hoover")
book2=Book(102,"Amma dairy lo konni pagelu","Ravi Mantri")
book1.display_book_details()
book2.display_book_details()