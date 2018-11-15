from string import ascii_letters as letters
import numpy as np

lower_case_letters = letters[:26]

def is_only_letters(word):

    for letter in word:
        if letter not in letters:
            return False
    return True


def has_no_duplicate_letter(word):
    word = list(word)
    bool = len(word) == len(set(word))
    return bool


def does_not_end_with_s(word):
    bool = word[-1] != 's'
    return bool


def word_to_list_of_bools(word):
    letter_list = list(word)
    bool_list = [1 if letter in letter_list else 0 for letter in lower_case_letters]
    return bool_list

def compute_word_overlap(word1, word2):
    '''
    computes the set overlap between two words of the same length
    :param word1: string
    :param word2: string
    :return: % overlap
    '''
    s1 = set(list(word1))
    s2 = set(list(word2))
    word_length = len(s1)
    overlap = len(s1.intersection(s2))
    #overlap_percentage = overlap/word_length
    return overlap


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()