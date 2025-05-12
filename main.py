import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = "books/" + sys.argv[1] + ".txt"
    try:
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        #num_chars = get_chars_dict(text)
        char_list = get_sorted_chars_list(text)
        print_report(filepath, num_words, char_list)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, num_words, char_list):
    REPORT_WIDTH = 33

    def print_header(title, separator):
        print(f"{' ' + title + ' ':{separator}^{REPORT_WIDTH}}")

    print_header("BOOKBOT", "=")
    print(f"Analyzing book found at {filepath}...")

    print_header("Word Count", "-")
    print(f"Found {num_words} total words")

    print_header("Character Count", "-")
    for item in char_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print_header("End", "=")

main()