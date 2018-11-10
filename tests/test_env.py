from game_classes import WordGame
from load_dictionary import return_words
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()

#######

def test_env_loads():
    w = return_words()
    w1 = WordGame(w, 5)

    print(w1.get_state())