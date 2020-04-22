class books:
    def __init__(self, pages=200, editorial='Tor books', autor='Robert Jordan',isbn=0):
        self.pages = pages
        self.editorial = editorial
        self.autor = autor
        self.isbn = isbn
    

class ebooks(books):
    def __init__(self, pages=200, editorial='Tor books', autor='Robert Jordan', isbn=0, kind='epub', weight=1024):
        super().__init__(pages, editorial, autor, isbn)
        self.kind = kind
        self.weight = weight


class printed_books(books):
    def __init__(self, pages=200, editorial='Tor books', autor='Robert Jordan', isbn=0, book_format='pocket'):
        super().__init__(pages, editorial, autor, isbn)
        self.book_format = book_format