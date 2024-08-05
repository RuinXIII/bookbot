def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_count = word_count(book_text)
    chars_dict = count_letter(book_text)
    dict_list = dict_to_list_of_dicts(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_count} found in the document")
    print_list(dict_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    letters = {}
    words = text.split()
    return len(words)

def count_letter(string):
    letters = {}
    for char in string:
        lower_char = char.lower()
        if lower_char in letters:
            letters[lower_char] += 1
        else:
            letters[lower_char] = 1

    return letters

def dict_to_list_of_dicts(d):
    char_list =  [{ "char" : k, "num": v} for k, v in d.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

def sort_dict(list):
    return list.sort

def print_list(wordlist):
    for obj in wordlist:
        if obj['char'].isalpha():
            print(f"The {obj['char']} was found {obj['num']} times")

main()
