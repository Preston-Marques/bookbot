def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = number_of_words(text)
    no_letters = number_of_letters(text)
    # print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")
    for i in no_letters:
        z = no_letters[i]
        print(f"The '{i}' character was found '{z}' times")
    print("--- End report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    words = text.split()
    return len(words)

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