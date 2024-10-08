def main():
    # path to book/text
    book_path = "./books/frankenstein.txt"

    # read contents of book_path
    text = read_book(book_path)

    # count number of words total
    words = count_words(text)

    # count frequency of each leter
    letters = count_letters(text)

    # generate report using two previous functions
    report = get_report(words, letters, book_path)

    print(report)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()

        return file_contents
    

def count_words(text):
    words = text.split()

    return len(words)


def count_letters(text):
    non_duplicate = text.lower()
    letters = {}

    for letter in non_duplicate:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters


def get_report(words, letters, book_path):
    chars_data = ""
    sorted_list = []

    # sort frequency list in descending order
    for letter in letters:
        if not letter.isalpha():
            continue
        sorted_list.append(letters[letter])
    sorted_list.sort(reverse=True)

    # generate character frequncy
    for char_count in sorted_list:
        for key, value in letters.items():
            if value == char_count:
                char = key
                char_data = f"The '{char}' character was found {char_count} times\n"
                chars_data += char_data

    # report
    return f"--- BEGIN REPORT OF {book_path} --- \n\n{words} words found in document \n\n{chars_data}\n--- END REPORT ---"

if __name__ == "__main__":
    main()