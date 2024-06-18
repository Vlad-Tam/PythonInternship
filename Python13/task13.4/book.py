from book_exceptions import PageCountError, AuthorError, PriceError, PublicationYearError


class Book:

    def __init__(self, count_of_pages: int, year: int, author: str, price: float):
        self.validate_count_of_pages(count_of_pages)
        self.validate_year(year)
        self.validate_author(author)
        self.validate_price(price)

        self.count_of_pages = count_of_pages
        self.year = year
        self.author = author
        self.price = price

    def validate_count_of_pages(self, count_of_pages: int) -> None:
        if not isinstance(count_of_pages, int) or count_of_pages <= 0:
            raise PageCountError("Pages count must be positive")

    def validate_year(self, year: int) -> None:
        if not isinstance(year, int) or year < 0:
            raise PublicationYearError("Year must be positive")

    def validate_author(self, author: str) -> None:
        if not isinstance(author, str) or len(author.strip()) == 0:
            raise AuthorError("Author must be not empty")

    def validate_price(self, price: (int, float)) -> None:
        if not isinstance(price, (int, float)) or price <= 0:
            raise PriceError("Price must be positive")
