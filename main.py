from stats import print_report, count_words, count_characters
import sys


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print_report(
        book_path,
        count_words(text),
        count_characters(text),
    )


main()
