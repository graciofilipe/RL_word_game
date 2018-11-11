from scripts.game_classes import WordGame
from scripts.load_dictionary import load_words, filter_words
from scripts.agent_class import Agent

import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()

def test_state_to_feature_vec():
    words = load_words()
    filtered_words = filter_words(word_list=words, length_of_word=5)
    a = Agent(epsilon=0.1, possible_actions=filtered_words)
    toy_state = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
                 (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0)}
    fv = a.state_to_feature_vec(state=toy_state)
    print(fv)


def test_rel_freq_of_dot_prod_of_bool_against_background():
    words = load_words()
    filtered_words = filter_words(word_list=words, length_of_word=5)
    a = Agent(epsilon=0.1, possible_actions=filtered_words)
    toy_state = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
                 (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0)}

    bool_word = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0)
    x = a.rel_freq_of_dot_prod_of_bool_against_background(bool=bool_word, list_of_bools=toy_state)
    print(x)


def test_state_action_to_feature_vec():
    words = load_words()
    filtered_words = filter_words(word_list=words, length_of_word=5)
    a = Agent(epsilon=0.1, possible_actions=filtered_words)
    toy_state = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
                 (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                 (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0)}

    a.bool_actions_taken = [(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0)]
    x = a.state_action_to_feature_vec(state=toy_state, action='shark')
    print(x)