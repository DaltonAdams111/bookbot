def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words = get_book_words(book_text)
    character_dict = get_character_count(book_text)
    sorted_characters = sort_characters(character_dict)
    book_report = get_book_report(sorted_characters, book_words)
    print(book_report)

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_book_words(book):
    return len(book.split())

def get_character_count(book):
    characters = {}
    for c in book:
        letter = c.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_characters(character_dict):
    letters = []
    for i in character_dict:
        if i.isalpha():
            letters.append({"letter": i, "num": character_dict[i]})
    return letters

def get_book_report(sorted_characters, book_words):
    report = f"--- Begin report of books/frankenstein.txt ---\n{book_words} words found in the document\n"
    for i in range(0, len(sorted_characters)):
        character = sorted_characters[i]["letter"]
        count = sorted_characters[i]["num"]
        report += (f"\nThe '{character}' character was found {count} times")
    report += "\n--- End report ---"
    return report

main()