
def number_of_words(text):
    words = text.split()
    return len(words)

def sorted_dict(dicts):
    return dict(sorted(dicts.items(), key=lambda item: item[1], reverse = True))