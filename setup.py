import random
import csv


def get_words_from_file(filename):
    """open file and return all lines as list."""
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def gen_word(prefixes, suffixes):
    """generate and return word as string."""
    word = ''
    for time in range(random.choice([1, 2, 3])):
        word += random.choice(prefixes)[0]
    word += random.choice(suffixes)[0]
    return word

if __name__ == '__main__':
    COUNT_WORDS = 1000

    list_prefix = get_words_from_file('library/prefix.csv')
    list_suffix = get_words_from_file('library/suffix.csv')

    for i in range(COUNT_WORDS):
        print(gen_word(list_prefix, list_suffix))
