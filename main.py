from stats import number_of_words
from stats import sorted_dict
import sys

def main():

    if (len(sys.argv) < 2):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    count = number_of_words(text)
    no_letters = number_of_letters(text)
    no_letters = sorted_dict(no_letters)


    #print(f"--- Begin report of {sys.argv[1]} ---")
    #print(f"{count} words found in the document\n")
    for i in no_letters:
        z = no_letters[i]
        #print(f"The '{i}' character was found '{z}' times")
        print(f"'{i}: {z}'")
    #print("--- End report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    


def number_of_letters(text):
    lowercase = text.lower()
    letters = { }
    for i in lowercase:
        if i in letters:
            letters[i] += 1
        else:
            if i.isalpha():
                letters[i] = 1
    return letters 


main()