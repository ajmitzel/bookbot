import sys
from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_character_count


def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        text = get_book_text(sys.argv[1])
        count = get_word_count(text)
        counts = get_character_count(text)
        sorted_counts = get_sorted_character_count(counts)
        print("========== BOOKBOT ==========")
        print("Analyzing book found at books/frankenstein.txt...")
        print("--------- Word Count ---------")
        print("Found {} total words".format(count))
        print("--------- Character Count ---------")
        for count in sorted_counts:
            print("{}: {}".format(count[0], count[1]))


main()