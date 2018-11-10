from game_classes import WordGame
from load_dictionary import return_words
import copy
import operator
import random

import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()

#######

w = return_words()
w1 = WordGame(w, 5)


def choose_best_next_word(game, words_to_sample):
    random.shuffle(game.words)
    available_words = game.words[:words_to_sample]
    available_words.append('shark')
    reduction_in_sols = {}
    for word in available_words:
        n_sols = []
        for potential_overlap in range(6):
            game_copy = copy.deepcopy(game)
            game_copy.add_constraint(word, potential_overlap)
            sol = game_copy.solve()
            print(word, potential_overlap, 'len sol:', len(sol))
            n_sols.append(len(sol))
        print(n_sols)
        number_of_solutions = sum(n_sols)
        print(word, number_of_solutions)
        reduction_in_sols[word] = number_of_solutions

    return reduction_in_sols


### game play
w1.add_constraint('shark', number_of_overlapping_letters=2)

d = choose_best_next_word(w1, 1)
best_word = min(d.items(), key=operator.itemgetter(1))[0]
print('chose:', best_word)


####
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s)
pr.print_stats(sort="cumtime")
print(s.getvalue())


#w1.add_constraint(best_word, number_of_overlapping_letters=)
