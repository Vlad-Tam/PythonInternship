class BookError(Exception):
    """Base book exceptions class"""
    pass


class PageCountError(BookError):
    """Invalid page count exception"""
    pass


class PublicationYearError(BookError):
    """Invalid page count exception"""
    pass


class AuthorError(BookError):
    """Invalid author exception"""
    pass


class PriceError(BookError):
    """Invalid price exception"""
    pass
