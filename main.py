from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

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

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_chars_dict(text)
    char_list = get_sorted_chars_list(text)

    print_report(filepath, num_words, char_list)
main()