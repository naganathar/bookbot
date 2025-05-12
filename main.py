from stats import get_num_words, get_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = "books/frankenstein.txt"
    text = get_book_text(frankenstein)
    num_words = get_num_words(text)
    num_chars = get_chars_dict(text)

    #print(f"{num_words} words found in the documents")
    print(f"{num_chars}")
main()