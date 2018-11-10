import pandas as pd

def return_words():
    word_table = pd.read_table('./data/words.txt', header=0)
    word_list = list(map(str, word_table['words_header']))

    word_list = [w.lower() for w in word_list]

    return word_list

