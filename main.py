import os
from stats import get_number_of_words, get_number_of_times_char_appear, sorted_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    with open(f"{path_to_book}") as f:
        book_content = f.read()

        num_words = get_number_of_words(book_content)
        dict_words = get_number_of_times_char_appear(book_content)
        sort_dict_list = sorted_dict(dict_words)

        text = f'''
            ============ BOOKBOT ============
            Analyzing book found at books/frankenstein.txt...
            ----------- Word Count ----------
            Found {num_words} total words
            --------- Character Count -------
        '''

        for i in sort_dict_list:
            char = i["char"]
            num = i["num"]

            if char.isalpha() == True:
                text += f'{char}: {num} \n'

        text += '''============= END ==============='''

        print(text)

if __name__ in "__main__":
    main()