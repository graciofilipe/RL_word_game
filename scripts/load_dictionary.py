import pandas as pd
from scripts.aux_functions import is_only_letters, has_no_duplicate_letter, does_not_end_with_s


def load_words():
    word_table = pd.read_table('../data/words.txt', header=0)
    word_list = list(map(str, word_table['words_header']))
    word_list = [w.lower() for w in word_list]
    return word_list


def filter_words(word_list, length_of_word):
    length_filtered_words = [w for w in word_list if len(w) == length_of_word]
    filtered_words = filter(is_only_letters, length_filtered_words)
    filtered_words = filter(has_no_duplicate_letter, filtered_words)
    filtered_words = filter(does_not_end_with_s, filtered_words)
    return list(set(list(filtered_words)))

