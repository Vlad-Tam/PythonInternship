from book_exceptions import BookError
from book import  Book


def main() -> None:
    try:
        book = Book(350, 2022, "Толстой Л.Н.", 500.0)
        print(book.count_of_pages, book.year, book.author, book.price)
    except BookError as e:
        print(f"Ошибка: {e}")

    try:
        book = Book(-10, 2022, "Толстой Л.Н.", 500.0)
    except BookError as e:
        print(f"Ошибка: {e}")

    try:
        book = Book(350, -2022, "Толстой Л.Н.", 500.0)
    except BookError as e:
        print(f"Ошибка: {e}")

    try:
        book = Book(350, 2022, "", 500.0)
    except BookError as e:
        print(f"Ошибка: {e}")

    try:
        book = Book(350, 2022, "Толстой Л.Н.", -500.0)
    except BookError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
