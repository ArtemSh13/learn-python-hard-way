def break_words(stuff):
    """This function parses the text into words"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """This function sorts words"""
    return sorted(words)


def print_first_word(words):
    """This function prints the first word after extraction"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """This function prints the last word after extraction"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """This function takes a whole sentence and returns sorted words"""
    words = break_words(sentence)
    return sorted(words)


def print_first_and_last(sentence):
    """This function prints the first and the last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """This function sorts words, and then prints the first and the last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
