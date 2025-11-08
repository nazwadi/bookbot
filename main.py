import sys

from stats import get_number_words
from stats import count_characters
from stats import get_sorted_list_dictionary

def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book_file = sys.argv[1]
    file_contents = get_book_text(path_to_book_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book_file}...")
    print("----------- Word Count ----------")
    num_words = get_number_words(file_contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_ch_dictionary = count_characters(file_contents)
    sorted_list = get_sorted_list_dictionary(num_ch_dictionary)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()

